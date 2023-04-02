from . import views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [

    path('list/', views.ListShoes.as_view({'get':'list' }), name='shoes_list'),
    path('list/new', views.ListNewShoes.as_view({'get':'list' }), name='shoes_list'),
    path('details/<int:pk>/', views.ListShoes.as_view({'get':'retrieve' }), name='shoes_details'),

    path('saved/<int:pk>/', views.UserSavedShoes.as_view({'get':'retrieve',}), name='savedshoes_details'),
    path('saved/remove/<int:pk>/', views.DeleteUserSavedShoes.as_view(), name='delete_savedshoes'),
    
    path('categories/', views.ListCategories.as_view(), name='categories_list'),
    path('brands/', views.ListBrands.as_view(), name='brands_list'),
]