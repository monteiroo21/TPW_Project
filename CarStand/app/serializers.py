from app.models import Profile, Group, Brand, CarModel, Car, Moto, Favorite, CarModel
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate_username(self, value):
        # If we are updating an existing user
        if self.instance and self.instance.pk:
            # If the username hasn't changed, just return it
            if value == self.instance.username:
                return value

            # If the username has changed, check for uniqueness
            if User.objects.exclude(pk=self.instance.pk).filter(username=value).exists():
                raise serializers.ValidationError("This username is already taken.")
        else:
            # Creating a new user, just check for uniqueness
            if User.objects.filter(username=value).exists():
                raise serializers.ValidationError("This username is already taken.")

        return value
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = UserSerializer(instance.user, data=user_data, partial=True)
            user_serializer.is_valid(raise_exception=True)
            user_serializer.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

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
