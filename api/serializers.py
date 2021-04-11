from rest_framework import serializers

from .models import (
    Isbn,
    Book,
    Character,
    Author
)


class IsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isbn
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']


class BookSerializer(serializers.ModelSerializer):
    isbn = IsbnSerializer(many=False)
    character = CharacterSerializer(many=True)
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
