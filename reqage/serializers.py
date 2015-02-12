###
#
# Serializers for reqage models
# ao 20150212
#
###
from rest_framework import serializers
from models import *
import reqage.models
from django.contrib.auth.models import User

class LexSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    parent = serializers.IntegerField()
    class Meta:
        model = Lex
        fields = ('pk', 'lextype', 'content', 'parent', 'created_by')

    # we need a special create override so we make the proper root DocThing object
    def create(self, validated_data):
        # save the parent's pk
        pnum=validated_data.get('parent', 0)
        if pnum>0:
            p = Lex.objects.get(pk=pnum)
        else:
            p = None

        # figure out what the lextype is and get the class
        lextype=validated_data.get('lextype')
        theclass=getattr(reqage.models,lextype)

        # create the new object (but remove the parent's key because it's not meaningful)
        validated_data.pop('parent', None)
        d=theclass.objects.create(**validated_data)

        if p is not None:
            # move the object's docthing to the proper parent
            d.docthing.move(p.docthing,'last-child')

        return d

class DocumentLineSerializer(LexSerializer):
    class Meta:
        model = DocumentLine
        fields = ('pk', 'lextype', 'content', 'parent', 'created_by', 'associated')

class RequirementSerializer(DocumentLineSerializer):
    class Meta:
        model = Requirement
        fields = DocumentLineSerializer.Meta.fields
    
class VerificationSerializer(DocumentLineSerializer):
    class Meta:
        model = Verification
        fields = ('pk', 'lextype', 'content', 'parent', 'created_by', 'associated', 'complete')

class DocumentSerializer(LexSerializer):
    class Meta:
        model = Document
        fields = ('pk', 'lextype', 'content', 'created_by')

class UserSerializer(serializers.ModelSerializer):
    lexs = serializers.PrimaryKeyRelatedField(many=True, queryset=Lex.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'lexs')