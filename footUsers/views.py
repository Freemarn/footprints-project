from django.shortcuts import render
from .serializers import UserDetailSerializer, RegisterSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import FootUser
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import generics, status

from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        data = serializer.validated_data
        access_token_str = data['access']

        access_token_obj = AccessToken(access_token_str)
        user_id=access_token_obj['user_id']
        user=FootUser.objects.get(id=user_id)
        user =  {'user.id':user.id, 'first_name':user.first_name, "last_name":user.last_name, 'email':user.email}

        return Response([serializer.validated_data, user], status=status.HTTP_200_OK,)
        
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
