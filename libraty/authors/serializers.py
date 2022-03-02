from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from .models import Author,Book,Biography

class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        # fields = ('first_name',)
        # exclude = ('first_name',)

class BiographyModelSerializer(ModelSerializer):
    # author = AuthorModelSerializer()
    class Meta:
        model = Biography
        fields = '__all__'

class BookModelSerializer(ModelSerializer):

    # authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'