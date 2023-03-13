from rest_framework import serializers
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from .models import Copy
from .models import Loan
from datetime import date, timedelta


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
        read_only_fields = ["id", "date_receipt", "date_devolution"]

    def create(self, validated_data):
        get_date_devolution = date.today() + timedelta(days=10)

        if get_date_devolution.weekday() == 5:
            return get_date_devolution + timedelta(days=2)
        elif get_date_devolution == 6:
            return get_date_devolution + timedelta(days=1)

        validated_data["date_devolution"] = get_date_devolution

        return Loan.objects.create(**validated_data)
