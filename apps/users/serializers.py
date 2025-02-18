from django.contrib.auth.models import User
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        """Override create to hash the password before saving"""
        user = User.objects.create_user(**validated_data) 
        return user
