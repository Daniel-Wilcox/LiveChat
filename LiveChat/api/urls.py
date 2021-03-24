from django.urls import path
from .views import UserProfileView, CreateUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', UserProfileView.as_view()),
    path('create-user', CreateUserView.as_view()),
    path('api-token-auth', obtain_auth_token, name='api-token-auth'),
]
