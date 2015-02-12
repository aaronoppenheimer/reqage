###
#
# Serializers for reqage models
# ao 20150212
#
###
from rest_framework import serializers
from models import *
from django.contrib.auth.models import User

class DocumentSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Document
        fields = ('pk', 'content', 'created_by')

    # we need a special create override so we make the proper root DocThing object
    def create(self, validated_data):
        print('woo!')
        docthing = DocThing.add_root(type='Document')
        docthing.save()
        validated_data['pk']=docthing.id
        return Document.objects.create(**validated_data)        
    

class RequirementSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='created_by.pk')
    class Meta:
        model = Requirement
        fields = ('pk', 'content', 'created_by')


class UserSerializer(serializers.ModelSerializer):
    lexs = serializers.PrimaryKeyRelatedField(many=True, queryset=Lex.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'lexs')