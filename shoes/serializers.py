from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Categories, Brand, Shoes, SavedShoes
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# shoes serializers
class ListShoesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shoes
        fields = [
            'name',
            'image',
            'price',
            'description',
            'category',
            'brand',
        ]
        extra_kwargs = {
            'name': {'read_only': True},
            'image': {'read_only': True},
            'price': {'read_only': True},
            'description': {'read_only': True},
            'category': {'read_only': True},
            'brand': {'read_only': True}
        }


# saved shoes serializers
class UserDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(read_only=True)

# class ShoeDataSerializer(serializers.Serializer):
#     shoes. = serializers.CharField()
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # image = serializers.ImageField(read_only=True)
    # price = serializers.IntegerField(read_only=True)
    # description = serializers.CharField(read_only=True)
    # category = serializers.CharField(read_only=True)
    # brand = serializers.CharField(read_only=True)

class UserSavedShoesSerializer(serializers.ModelSerializer):
    user = UserDataSerializer( read_only=True)
    shoes = ListShoesSerializer(read_only=True, many=True)
    shoes = serializers.CharField()
    
    class Meta:
        model = SavedShoes
        # fields = '__all__'
        fields = [
            'user', 
            'shoes'
        ]


# Categories serializers
class ListCategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = '__all__'
        extra_kwargs = {
            'name': {'read_only': True},
        }

# Brand serializers
class ListBrandsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'
        extra_kwargs = {
            'name': {'read_only': True},
            'logo': {'read_only': True}
        }
