from rest_framework import serializers
from books.models import Book, Gender


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "pages",
            "created_at",
            "updated_at",
            "followers",
            "book_genders"
        ]
        extra_kwargs = {
            "created_at": {"write_only": True},
            "updated_at": {"write_only": True},
            "followers": {"write_only": True},
            "book_genders": {"write_only": True},
        }


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = [
            "id"
            "name"
        ]
