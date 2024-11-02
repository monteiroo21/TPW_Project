from django.shortcuts import render, redirect, get_object_or_404
from app.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import Group, Brand, Profile
from django.db.models import Q
from app.loadBackup import *
# Create your views here.

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        Profile.objects.create(
            user=user,
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            email=form.cleaned_data.get('email')
        )
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        print(form.errors)
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('index')
    else:
        print(form.errors)
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index') 

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

# def brands(request):
#     groups = Group.objects.prefetch_related('brands')
#     context = {'groups': groups}
#     return render(request, 'brands.html', context)

def brands(request):
    groups = Group.objects.filter(name__iendswith='group').prefetch_related('brands')

    independent_brands = Brand.objects.filter(
        Q(group__isnull=True) | ~Q(group__name__iendswith='group')
    )
    context = {
        'groups': groups,
        'independent_brands': independent_brands,
    }
    return render(request, 'brands.html', context)

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    context = {'brand': brand}
    return render(request, 'brand_detail.html', context)

    