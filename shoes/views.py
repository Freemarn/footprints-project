from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django_filters import rest_framework as filters2
from .filters import ListShoesFilter
from rest_framework.pagination import PageNumberPagination
from datetime import timedelta, datetime
# Create your views here.

from .models import Categories, Brand, Shoes, SavedShoes
from .serializers import ListShoesSerializer, UserSavedShoesSerializer, UserSave_ShoesSerializer, ListCategoriesSerializer, ListBrandsSerializer


# shoes view
class ListShoesPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'ListShoes_size'

class ListShoes(viewsets.ModelViewSet ):
    queryset = Shoes.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ListShoesSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter, filters2.DjangoFilterBackend,)
    filterset_class = ListShoesFilter
    search_fields = ['description', 'name',]
    ordering_fields = ['price', 'name']
    pagination_class = ListShoesPagination
    lookup_field = 'pk'

class ListNewShoes(viewsets.ModelViewSet ):
    queryset = Shoes.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ListShoesSerializer

    filter_backends = (filters.SearchFilter, filters2.DjangoFilterBackend,)
    filterset_class = ListShoesFilter
    search_fields = ['description', 'name',]
    pagination_class = ListShoesPagination
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(created_at__gte=(datetime.now() - timedelta(days=30)))
        serializer = self.serializer_class(queryset, many=True, context={'request': request}, read_only=True)
        page = self.paginate_queryset(serializer.data)

        if page is not None:
            return self.get_paginated_response(serializer.data)

class SavedShoesPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'ListSavedShoes'
    
class UserSavedShoes(viewsets.ModelViewSet):
    queryset = SavedShoes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSavedShoesSerializer
    pagination_class = SavedShoesPagination
    lookup_field = 'pk'
    
    def list(self, request, *args, **kwargs):
        
        
        queryset = self.queryset.filter(user=self.request.user)
        serializer = self.serializer_class(queryset, many=True, context={'request': request}, read_only=True)
        page = self.paginate_queryset(serializer.data)

        if page is not None:
            return self.get_paginated_response(serializer.data)
        # else:
            # serializer = self.serializer_class([], many=True, context={'request': request}, read_only=True)
            # return Response(serializer.data)
            
    def retrieve(self, request, *args, **kwargs):
        if(self.request.user.savedshoes_set.values().filter(id =self.get_object().pk).exists()):
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            serializer = self.serializer_class([], many=True, context={'request': request}, read_only=True)
            return Response(serializer.data)



class UserSave_Shoes(viewsets.ModelViewSet):
    queryset = SavedShoes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSave_ShoesSerializer
    serializer = UserSave_ShoesSerializer
    lookup_field = 'pk'


class DeleteUserSavedShoes(generics.DestroyAPIView ):
    queryset = SavedShoes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSavedShoesSerializer
    lookup_field = 'pk'

    def perfom_destroy(self, instance):
        if(self.request.user.savedshoes_set.values().filter(id =self.get_object().pk).exists()):
            super().perform_destroy()

class ListCategories(generics.ListAPIView):
    queryset = Categories.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ListCategoriesSerializer

class ListBrands(generics.ListAPIView):
    queryset = Brand.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ListBrandsSerializer