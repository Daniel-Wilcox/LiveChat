from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from myUsers.permission import PublicViewPermissions


# Users
from myUsers.serializers import UserProfileSerializer, CreateUserSerializer, UserProfilePageSerializer
from myUsers.models import UserProfile


# Create your views here.


# Read only permissions


# GET request to get all user's basic info ('username', 'user_bio', 'date_joined', 'is_active', 'is_hosting')
@api_view(['GET', ])
@permission_classes([PublicViewPermissions])
def GetPublicUserProfile(request, userPage):
    # userPage variable must have the same name as /api/<str:userPage>

    try:
        userPage = UserProfile.objects.get(username=userPage)
    except:
        return Response({"user not found": "invalid username"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer_class = UserProfilePageSerializer(userPage)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
    return Response({"bad request method": "only get request method"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileView2(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
