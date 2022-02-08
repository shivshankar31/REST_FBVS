from dataclasses import fields
from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only = True, many = True)
    class Meta:
        model = Author
        fields = '__all__'

        