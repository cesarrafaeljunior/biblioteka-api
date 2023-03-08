from rest_framework import serializers
from .models import Copy
# from books.models import Book 


class CopySerializer(serializers.ModelSerializer):
    # book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = [
            "id",
            "ammounts_of_copies",
            "copies_avaliable",
            "book",
        ]
    