from rest_framework import serializers
from .models import Book


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'description','image', 'category','favorite', 'pages','authors']
