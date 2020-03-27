from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Trip, Category


class TripsSerializer(serializers.ModelSerializer):
    """
    This serializer serializes the trip data
    """
    class Meta:
        model = Trip
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    """
    This serializer serializes the category data
    """
    class Meta:
        model = Trip
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")