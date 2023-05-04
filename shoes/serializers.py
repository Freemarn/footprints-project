from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Categories, Brand, Shoes, SavedShoes
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.fields import CurrentUserDefault
from footUsers.models import FootUser
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

# shoes serializers

class ListShoesSerializer(serializers.ModelSerializer):
    category = ListCategoriesSerializer(read_only=True, many=True)

    class Meta:
        model = Shoes
        fields = [
            'id',   
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
            'category': {'read_only': True, },
            'brand': {'read_only': True}
        }


# saved shoes serializers
class UserDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(read_only=True)

class UserSavedShoesSerializer(serializers.ModelSerializer):
    user = UserDataSerializer( read_only=True)
    shoes = ListShoesSerializer(read_only=True,)
    
    class Meta:
        model = SavedShoes
        fields = [
            'id',
            'shoes',
            'user', 
        ]


class UserSave_ShoesSerializer(serializers.Serializer):
    user = serializers.CharField(  required=True)
    shoes = serializers.CharField(  required=True)

    def create(self, validated_data):
        Shoe_id = validated_data["shoes"]
        user_id = validated_data["user"]
        shoe_instance = Shoes.objects.get(id=Shoe_id)
        footUser_instance = FootUser.objects.get(id=user_id)
        validated_data["shoes"] = shoe_instance
        validated_data["user"] = footUser_instance
        obj = SavedShoes(**validated_data)
        obj.user = footUser_instance
        obj.shoes = shoe_instance
        obj.save()
        return obj


