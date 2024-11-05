from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from app.forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from .models import Group, Brand, Profile
from django.db.models import Q
from app.loadBackup import *
# Create your views here.

def sign_up(request):
    if request.method == "POST":
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
    else:
        form = SignUpForm()  
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user!=None:
            login(request, user)
            return redirect('index')
    
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index') 

def index(request):
    for k,v in request.session.items():
        print(k,v)
    context = {}
    return render(request, 'index.html', context)

def cars(request):
    #creategroups()
    carsList=Car.objects.all()
    context = {"cars":carsList}
    return render(request, 'cars.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    isSelected = False
    isBuyed = None
    
    
    if "favoriteCarList" not in request.session:
        request.session["favoriteCarList"] = []

    
    isFavorite = car_id in request.session["favoriteCarList"]

    
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        isSelected = car.interestedCustomers.filter(id=profile.id).exists()
        isBuyed = car.purchaser is not None and car.purchaser.id == profile.id


    
    if request.POST:
        favoriteCarList = request.session["favoriteCarList"]
        if isFavorite:
            favoriteCarList.remove(car_id)
        else:
            favoriteCarList.append(car_id)
        
        request.session["favoriteCarList"] = favoriteCarList
        isFavorite = car_id in request.session["favoriteCarList"]

    
    context = {
        "car": car,
        "isSelected": isSelected,
        "isBuyed": isBuyed,
        "isFavorite": isFavorite,
    }
    print(request.session["favoriteCarList"] )
    return render(request, "car_detail.html", context)


def motorbike_detail(request, moto_id):
    moto = get_object_or_404(Moto, id=moto_id) 
    return render(request, 'motorbike_detail.html', {'moto': moto})

def selectCar(request, car_id):
    if not request.user.is_authenticated:
        return redirect("login")
    car = get_object_or_404(Car, id=car_id) 
    profile = get_object_or_404(Profile, user=request.user) 
    print(profile)
    car.interestedCustomers.add(profile)
    print(car)
    return redirect('car_detail', car_id=car.id)  

def managerConfirm(request):
    if not request.user.is_authenticated:
        return redirect("login")
    print(request.user.username)
    if request.user.username!='admin':
        return redirect("index")
    listForAccept=[]
    cars=Car.objects.all()
    for car in cars:
        for profile in car.interestedCustomers.all():
            listForAccept.append({"car":car,"profile":profile})
    context = {"listForAccept":listForAccept}
    return render(request, 'managerConfirm.html', context)

def approve(request, car_id,profile_id):
    car = get_object_or_404(Car, id=car_id) 
    profile = get_object_or_404(Profile, id=profile_id) 

    car.interestedCustomers.clear()  
    car.purchaser=profile
    car.save()
    
    return redirect('managerConfirm')  

def negate(request, car_id,profile_id):
    car = get_object_or_404(Car, id=car_id) 
    profile = get_object_or_404(Profile, id=profile_id) 

    car.interestedCustomers.remove(profile)
    
    return redirect('managerConfirm')  

def motorbikes(request):
    motosList=Moto.objects.all()
    context = {"motos":motosList}
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

    