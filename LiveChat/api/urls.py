from django.urls import path
from .views import UserProfileView, CreateUserView, GetPublicUserProfile
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserProfileView.as_view()),
    path('<str:userPage>', GetPublicUserProfile),
    # path('create-user/', CreateUserView.as_view()),
    # this view requires an authToken when adding 'obtain_auth_token'
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]
