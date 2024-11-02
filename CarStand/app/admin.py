from django.contrib import admin
from app.models import Profile, Group, Brand,CarModel,Moto

# Register your models here.

admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Moto)
