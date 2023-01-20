from django.contrib.auth import get_user_model
from django.urls import path
from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer

User = get_user_model()


class UserCreateAPI(CreateAPIView):
    queryset = User.objects.all
    serializer_class = UserSerializer


urlpatterns = [
    path("", UserCreateAPI.as_view()),
]
