from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
# from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# # Create your models here.
# class StandManager(UserManager):
#     def create_user(self, username, password):
#         pass
#     def create_superuser(self, username: str, email: str | None, password: str | None):
#         pass


# class Client(AbstractUser):
#     pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.user.username
    

class Group(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=30)
    website = models.URLField()
    logo = models.ImageField(upload_to='./static/imgs/', null=True, blank=True)
    headquarters = models.ImageField(upload_to='./static/imgs/', null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=30)
    website = models.URLField()
    # cellPhone = PhoneNumberField(null=False, blank=False, unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    cellPhone = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    group = models.ForeignKey(Group, related_name='brands', on_delete=models.CASCADE)
    description = models.TextField()
    logo = models.ImageField(upload_to='./static/imgs/')

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, related_name='brand_cars', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    base_price = models.FloatField()
    specifications = models.TextField()
    releaseYear = models.PositiveIntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2024)])

    def __str__(self):
        return self.name + ", " + self.brand.name

class Car(models.Model):
    model = models.ForeignKey(CarModel, related_name='model_cars', on_delete=models.CASCADE)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2024)])
    new = models.BooleanField(default=True)
    kilometers = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='./static/imgs/cars',default="./static/imgs/motos/aprilia_rs660.png")
    interestedCustomers=models.ManyToManyField(Profile, blank=True,default=None,related_name='interested_in_cars')
    purchaser=models.ForeignKey(Profile, null=True,default=None, blank=True, related_name='purchased_cars', on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=20, default="Black") 
    doors = models.IntegerField(default=4)
    electric = models.BooleanField(default=False)

    def __str__(self):
        return self.model.name + ", " + self.model.brand.name

class Moto(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2024)])
    new = models.BooleanField(default=True)
    kilometers = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='./static/imgs/motos',default="./static/imgs/motos/aprilia_rs660.png")
    interestedCustomers=models.ManyToManyField(Profile, blank=True,default=None,related_name='interested_in_motos')
    purchaser=models.ForeignKey(Profile, null=True, default=None, blank=True, related_name='purchased_motos', on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=20, default="Black") 

