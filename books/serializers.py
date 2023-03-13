from rest_framework import serializers
from django.shortcuts import get_object_or_404
from books.models import Book, Gender


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = [
            "id",
            "name"
        ]


class BookSerializer(serializers.ModelSerializer):

    book_genders = GenderSerializer(many=True)

    def create(self, validated_data: dict) -> Book:
        gender_list = validated_data.pop("book_genders")

        genders = []

        for gender in gender_list:
            name = gender["name"]
            gender_object = Gender.objects.filter(name__contains=name).first()

            if not gender_object:
                gender_object = Gender.objects.create(name=name)
            genders.append(gender_object)

        book = Book.objects.create(**validated_data)
        book.book_genders.set(genders)
        return book

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
        depth = 1
