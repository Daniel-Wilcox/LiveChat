from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'date_of_birth',
                  'date_joined', 'is_active', 'is_hosting']


class UserProfilePageSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['username', 'user_icon', 'user_bio',
                  'date_joined', 'is_active', 'is_hosting']


class RegisterUserSerializer(serializers.ModelSerializer):
    confirmed_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password',
                  'confirmed_password', 'date_of_birth', 'email']

    def save(self, validated_data):
        user = UserProfile(
            username=validated_data['username'],
            email=validated_data['email'],
            date_of_birth=validated_data['date_of_birth'],
        )
        password = validated_data['password']
        confirmed_password = validated_data['confirmed_password']

        if password != confirmed_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})

        user.set_password(password)
        user.save()
        return user
