from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', views.RegisterUser.as_view(), name='SignUp'),
    path('details/<int:pk>/', views.UserDetail.as_view(), name='user_details'),
    path('update/<int:pk>/', views.EditUser.as_view(), name='update_user'),
    path('delete/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
]