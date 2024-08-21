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
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def sendMail(email, customer_name, html, recipient_email_list):
    from_email = 'admin@footprints.name.ng'
    subject = 'Footprints'

    context = {
        'Customer_name': customer_name,
        'email': email,
    }

    html_content = render_to_string(html, context)
    text_content = strip_tags(html_content)  # Create plain text version

    # Create the email message
    email = EmailMultiAlternatives(subject, text_content, from_email, recipient_email_list)
    email.attach_alternative(html_content, "text/html")
    email.send()
    
    



class RegisterUser(generics.CreateAPIView):
    queryset = FootUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        fullName = f"{first_name} {last_name}"
        details =  f"""
            name: {fullName}
            email: {email}
        """
        print(details)
        # you can add all admin email in the list []
        sendMail(email, fullName, "new_user.html" , ['alikaprosper94@gmail.com', 'Footprintsshoehub@gmail.com']) #for admins
        # for newly registerd users
        sendMail(email, fullName, "welcome.html", [email])
        return self.create(request, *args, **kwargs)






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
        user =  {'user_id':user.id, 'first_name':user.first_name, "last_name":user.last_name, 'email':user.email}

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
