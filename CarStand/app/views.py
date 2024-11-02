from django.shortcuts import render, redirect, get_object_or_404
from app.forms import SignUpForm
from django.contrib.auth import login, authenticate
from .models import Group, Brand
from app.loadBackup import *
# Create your views here.

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    Group.objects.all().delete()
    Brand.objects.all().delete()
    Moto.objects.all().delete()
    CarModel.objects.all().delete()
    creategroups()
    createBrandCarro()
    createBrandMota()
    createMotas()
    context = {}
    return render(request, 'index.html', context)

def cars(request):
    #creategroups()
    context = {}
    return render(request, 'cars.html', context)

def motorbikes(request):
    context = {}
    return render(request, 'motorbikes.html', context)

def brands(request):
    groups = Group.objects.prefetch_related('brands')
    context = {'groups': groups}
    return render(request, 'brands.html', context)

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    context = {'brand': brand}
    return render(request, 'brand_detail.html', context)

    