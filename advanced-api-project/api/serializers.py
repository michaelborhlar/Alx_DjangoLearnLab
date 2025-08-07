from rest_framework import serializers
from .models import Book
from .models import Author
from datetime import datetime



class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):

    name = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'name']

