from app.models import Profile, Group, Brand, CarModel, Car, Moto, Favorite
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password']
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'email']


class GroupSerializer(serializers.ModelSerializer):
    brands = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'email', 'country', 'website', 'logo', 'headquarters', 'brands']


class BrandSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Brand
        fields = ['id', 'name', 'email', 'country', 'website', 'cellPhone', 'group', 'description', 'logo']


class CarModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = CarModel
        fields = ['id', 'brand', 'name', 'base_price', 'specifications', 'releaseYear', 'vehicle_type']


class CarSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    interestedCustomers = ProfileSerializer(many=True)
    purchaser = ProfileSerializer()

    class Meta:
        model = Car
        fields = [
            'id', 'model', 'year', 'new', 'kilometers', 'price', 'image',
            'interestedCustomers', 'purchaser', 'color', 'doors', 'electric'
        ]
        extra_kwargs = {
            'interestedCustomers': {'required': False},
            'purchaser': {'required': False, 'allow_null': True},
            'image': {'required': False, 'allow_null': True},  # Permitir null
            'color': {'required': False, 'allow_null': True},
            'doors': {'required': False, 'allow_null': True},
            'electric': {'required': False, 'allow_null': True}
        }

class MotoSerializer(serializers.ModelSerializer):
    model = CarModelSerializer()
    interestedCustomers = ProfileSerializer(many=True)
    purchaser = ProfileSerializer()

    class Meta:
        model = Moto
        fields = [
            'id', 'model', 'year', 'new', 'kilometers', 'price', 'image',
            'interestedCustomers', 'purchaser', 'color'
        ]
        extra_kwargs = {
            'interestedCustomers': {'required': False},
            'purchaser': {'required': False, 'allow_null': True},
            'image': {'required': False, 'allow_null': True},
            'color': {'required': False, 'allow_null': True}
        }

class FavoriteSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    favoritesCar = CarSerializer(many=True)
    favoritesMoto = MotoSerializer(many=True)

    class Meta:
        model = Favorite
        fields = ['id', 'profile', 'favoritesCar', 'favoritesMoto']
