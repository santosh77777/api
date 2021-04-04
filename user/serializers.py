from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if (email and User.objects.filter(email=email).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(email=email)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):

    shifts = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['email', 'shifts']
        

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'