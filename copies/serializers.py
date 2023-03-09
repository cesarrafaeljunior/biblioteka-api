from rest_framework import serializers
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from .models import Copy
from .models import Loan
from datetime import timedelta


class CopySerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)

    book = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = [
            "id",
            "ammounts_of_copies",
            "copies_avaliable",
            "book",
        ]

    def get_book(self, obj) -> str:
        return obj.book.title


class LoanSerializer(serializers.ModelSerializer):
    copy = CopySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    date_devolution = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = [
            "id",
            "date_receipt",
            "date_devolution",
            "is_receipt",
            "price",
            "copy",
            "user",
        ]

    def get_date_devolution(self, obj):
        date_devolucion = self.date_receipt + timedelta(days=10)

        if date_devolucion.weekday() == 5:
            return date_devolucion + timedelta(days=2)
        elif date_devolucion == 6:
            return date_devolucion + timedelta(days=1)

        return date_devolucion
