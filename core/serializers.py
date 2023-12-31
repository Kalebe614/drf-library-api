from rest_framework import serializers
from .models import PublisherModel, AuthorModel, BookModel
from django.urls import reverse

class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model= PublisherModel
        fields = ['id', 'name', 'description', 'created', 'updated']

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='books-detail'
    )
    class Meta:
        model = AuthorModel
        fields = ['id', 'first_name', 'last_name','about', 'created', 'updated', 'books']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = '__all__'
        