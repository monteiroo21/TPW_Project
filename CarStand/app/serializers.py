from app.models import Profile, Group, Brand, CarModel, Car, Moto, Favorite, CarModel
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

class MinimalGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class MinimalCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name']


class BrandSerializer(serializers.ModelSerializer):
    group = MinimalGroupSerializer()
    models = MinimalCarModelSerializer(many=True)
    class Meta:
        model = Brand
        fields = ['id', 'name', 'email', 'country', 'website', 'cellPhone', 'description', 'logo', 'group', 'models']


class GroupSerializer(serializers.ModelSerializer):
    brands = BrandSerializer(many=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'email', 'country', 'website', 'logo', 'headquarters', 'brands']


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

class ModelSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    motos = MotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        fields = ['id', 'name', 'description', 'cars', 'motos']



class FavoriteSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    favoritesCar = CarSerializer(many=True)
    favoritesMoto = MotoSerializer(many=True)

    class Meta:
        model = Favorite
        fields = ['id', 'profile', 'favoritesCar', 'favoritesMoto']
