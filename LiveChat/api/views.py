from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


# Users
from myUsers.serializers import UserProfileSerializer, CreateUserSerializer
from myUsers.models import UserProfile


# Create your views here.

class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CreateUserView(APIView):
    pass
#     serializer_class = CreateUserSerializer

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             username = serializer.data.get('username')
#             email = serializer.data.get('email')
#             date_of_birth = serializer.data.get('date_of_birth')
#             user_bio = serializer.data.get('user_bio')

#             # Check if user exists
#             queryset = UserProfile.objects.filter(username=username)
#             if queryset.exists():
#                 return Response({'Bad Request': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

#             # Check if email exists
#             queryset = UserProfile.objects.filter(email=email)
#             if queryset.exists():
#                 return Response({'Bad Request': 'Email is already in use.'}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 user = UserProfile(username=username, email=email,
#                                    date_of_birth=date_of_birth, user_bio=user_bio)
#                 user.save()
#                 return Response(UserProfileSerializer(user).data, status=status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
