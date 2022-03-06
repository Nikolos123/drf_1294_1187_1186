from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer



class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')


class UserBasedModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')

