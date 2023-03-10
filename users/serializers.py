from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:

        if "is_collaborator" in validated_data.keys() and validated_data["is_collaborator"]:
            validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_collaborator",
            "is_blocked",
            "unlock_date",
        ]
        extra_kwargs = {"password": {"write_only": True}}
