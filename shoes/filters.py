
from django import forms
from django.contrib.auth.models import User, Group
from .models import Shoes, Categories, Brand
from django_filters import rest_framework as filters
from django.db.models import Sum
# from ledger.serializers import  CashFlow_Ratios_Serializer

CATEGORY_CHOICES = []
for i in Categories.objects.all():
    CATEGORY_CHOICES.append((i, f'{i.id}'))
    
BRAND_CHOICES = []
for i in Brand.objects.all():
    BRAND_CHOICES.append((i, f'{i.id}'))

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

# class LedgeFilter(filters.FilterSet):
#     date_range = filters.DateRangeFilter(field_name='created_at')
#     start_date = filters.DateFilter(field_name='created_at',lookup_expr=('gte'),) 
#     end_date = filters.DateFilter(field_name='created_at',lookup_expr=('lte'))
#     # print('fillter is set....................................................')

#     class Meta:
#         model = CashFlow
#         fields = [
#             'start_date',
#             'end_date',
#             'date_range',
#             'category',
#             'cashStream',
#         ] 

# class LedgeRatio(filters.FilterSet):
#     date_range = filters.DateRangeFilter(field_name='created_at')
#     start_date = filters.DateFilter(field_name='created_at',lookup_expr=('gte'),) 
#     end_date = filters.DateFilter(field_name='created_at',lookup_expr=('lte'))

#     class Meta:
#         model = CashFlow
#         fields = [
#             'start_date',
#             'end_date',
#             'date_range',
#         ] 
    
    # # calc...............................
    # def to_representation(self, instance):
    #     original_representation = super().to_representation(instance)

    #     representation = {
    #         'total': self.get_total_Credit(instance),
    #         'detail': original_representation,
    #     }

    #     return representation

    # def get_total_Credit(self, obj):
    #     totalCredit = CashFlow.objects.aggregate(Sum('Credit'))

    #     return totalCredit['total_salary']

