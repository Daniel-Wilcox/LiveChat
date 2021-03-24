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


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'date_of_birth', 'user_bio')
