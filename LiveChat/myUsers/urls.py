from django.urls import path
from .views import UserProfileView, CreateUserView

urlpatterns = [
    path('', UserProfileView.as_view()),
    path('create-user', CreateUserView.as_view()),
]
