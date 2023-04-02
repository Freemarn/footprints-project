from django.shortcuts import render
from .serializers import UserDetailSerializer, RegisterSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework.views import APIView
import jwt
from .models import FootUser
from datetime import datetime, timedelta
from django.conf import settings
import random
import string
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class RegisterUser(generics.CreateAPIView):
    queryset = FootUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = FootUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

class EditUser(generics.UpdateAPIView):
    queryset = FootUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class DeleteUser(generics.DestroyAPIView):
    queryset = FootUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer
