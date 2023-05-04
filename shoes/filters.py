
from django import forms
from django.contrib.auth.models import User, Group
from .models import Shoes, Categories, Brand
from django_filters import rest_framework as filters
from django.db.models import Sum
# from ledger.serializers import  CashFlow_Ratios_Serializer

CATEGORY_CHOICES = []
for i in Categories.objects.all():
    CATEGORY_CHOICES.append((i.id, f'{i.id}'))
    
BRAND_CHOICES = []
for i in Brand.objects.all():
    BRAND_CHOICES.append((i.id, f'{i.id}'))

class ListShoesFilter(filters.FilterSet):
    category = filters.TypedMultipleChoiceFilter(field_name='category', choices=CATEGORY_CHOICES)
    brand = filters.TypedMultipleChoiceFilter(field_name='brand', choices=BRAND_CHOICES)
    # print('fillter is set....................................................')

    class Meta:
        model = Shoes
        fields = [
            'category',
            'brand',
        ] 


