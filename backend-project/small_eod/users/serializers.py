from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id"]
        fields = ["password", "username", "email", "first_name", "last_name", "id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class RequestSerializer(serializers.Serializer):
    url = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    expires_in = serializers.IntegerField(default=api_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
    refresh_token = serializers.CharField()


class RefreshTokenRequestSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
