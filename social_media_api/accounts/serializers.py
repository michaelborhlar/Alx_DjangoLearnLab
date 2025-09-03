from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    password=serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = "__all__"

        def create(self, validated_data):
            user=get_user_model().objects.create_user

            Token.objects.create(user=user)
            return user
 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

