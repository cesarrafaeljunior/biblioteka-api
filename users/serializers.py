from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        try:
            validated_data["is_collaborator"] == True
            validated_data["is_superuser"] = True
        except:
            ...

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        try:
            password = validated_data.pop("password")
            instance.set_password(password)

        except:
            ...

        for key, value in validated_data.items():
            setattr(instance, key, value)

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
        ]
        extra_kwargs = {"password": {"write_only": True}}
