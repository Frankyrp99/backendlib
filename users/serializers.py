from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers
from .models import UserProfile

# clase que se encarga de transformar de json a User y de User a json


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["role"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","nombre", "apellidos", "email", "password", "role"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.role == "admin":
            representation["password"] = instance.password
        return representation

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, _, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance=validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(
            request=self.context.get("request"), username=email, password=password
        )

        if not user:
            raise serializers.ValidationError(
                "No se pudo autenticar", code="auhorization"
            )

        data["user"] = user
        return data
