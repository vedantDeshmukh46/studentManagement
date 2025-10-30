from django.http import HttpRequest, HttpResponse
from rest_framework import generics
from .models import User
from .serializer import UserSerializer

# get users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# user by id -get , update , delete
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def helloWorld(HttpRequest):
    return HttpResponse("Hello World")
