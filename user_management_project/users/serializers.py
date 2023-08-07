from rest_framework import serializers

from .validators import ValidateUsername
from .models import User

class UserSerializer(ValidateUsername, serializers.ModelSerializer):
    """Serializer for users' data."""

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio')


class SignUpSerializer(ValidateUsername, serializers.Serializer):
    """Serializer for users' data for sign up."""

    username = serializers.CharField(
        required=True,
        max_length=150,
    )
    email = serializers.EmailField(required=True, max_length=254)


class TokenSerializer(ValidateUsername, serializers.Serializer):
    """Serializer for users' data for getting a token."""
    username = serializers.CharField(
        required=True,
        max_length=150,
    )
    confirmation_code = serializers.CharField(required=True)
