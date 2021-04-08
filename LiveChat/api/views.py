from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from myUsers.permission import PublicViewPermissions


# Users
from myUsers.serializers import UserProfileSerializer, RegisterUserSerializer, UserProfilePageSerializer
from myUsers.models import UserProfile


# Create your views here.


# Read only permissions

# @api_view(['request.method', ])
# @permission_classes([PublicViewPermissions, PublicViewPermissions])
# @authentication_classes([TokenAuthentication, ])
# def name_of_functional_view(request, URL_ID_NAME):


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
    return Response({"bad request method": "only GET request method"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes([AllowAny])
def SignUpUser(request):

    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save(request.data)
            data['response'] = "Successfully registered new user"
            data['username'] = user.username
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({"bad request method": "only POST request method"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes([PublicViewPermissions])
def CheckUserEmailExists(request, userEmail):

    try:
        userEmail.index("@")
        emailRegex = r'({0})(\.[a-zA-Z]{{2,3}}){{1,2}}'.format(userEmail)

        try:
            userEmail = UserProfile.objects.get(email__regex=emailRegex)
            return Response({"Email_free": False}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"Email_free": True}, status=status.HTTP_200_OK)

    except:
        return Response({"Email format is not valid": "Bad formatting"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method != 'GET':
        return Response({"bad request method": "only get request method"}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileView2(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
