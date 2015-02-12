###
#
# Serializers for reqage models
# ao 20150212
#
###
from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class LexSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    parent = serializers.IntegerField()
    class Meta:
        model = Lex
        fields = ('pk', 'reqtype', 'content', 'parent', 'created_by')

    # we need a special create override so we make the proper root DocThing object
    def create(self, validated_data):
        # save the parent's pk
        pnum=validated_data.get('parent', '')
        if pnum=='':
            raise()

        # create the new object (but remove the parent's key because it's not meaningful)
        validated_data.pop('parent', None)
        d=Lex.objects.create(**validated_data)

        # now use the parent key to place the Lex into the document hierarchy
        p = Lex.objects.get(pk=pnum)
        Lex.create_docthing(d,parent=p)
        return d



class DocumentSerializer(LexSerializer):
    class Meta:
        model = Document
        fields = ('pk', 'content', 'created_by')

    # we need a special create override so we make the proper root DocThing object
    def create(self, validated_data):
        d=Document.objects.create(**validated_data)
        Lex.create_docthing(d,parent=None)
        return d


class UserSerializer(serializers.ModelSerializer):
    lexs = serializers.PrimaryKeyRelatedField(many=True, queryset=Lex.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'lexs')