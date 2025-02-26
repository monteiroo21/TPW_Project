from django.shortcuts import render, redirect, get_object_or_404
from app.forms import ConfirmFilter, CreateMoto, MotoSortAndFilter, SignUpForm, LoginForm, GroupSearchForm, BrandSearchForm,CarSortAndFilter,CreateCar,CreateCarModel, UpdateCar, ProfileForm, UpdateMoto
from django.contrib.auth import login, authenticate, logout
from .models import Group, Brand, Profile,Favorite,Car,CarModel,Moto
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

# Filters a queryset of vehicles based on a search string matching brand and model names.
def filterByBrandAndName(name,listVehicle):
    search_terms = name.split()
    name_query = Q()
    match_found = False
    
    for i in range(len(search_terms), 0, -1):
        possible_brand = " ".join(search_terms[:i])
        remaining_terms = search_terms[i:]

        brand_query = Q(model__brand__name__icontains=possible_brand)
        model_query = Q()

        for term in remaining_terms:
            model_query &= Q(model__name__icontains=term)

        if remaining_terms:
            name_query = brand_query & model_query
        else:
            name_query = brand_query | Q(model__name__icontains=possible_brand)
        
        if listVehicle.filter(name_query).exists():
            match_found = True
            listVehicle = listVehicle.filter(name_query)
            break

    if not match_found:
        generic_query = Q()
        for term in search_terms:
            generic_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
        listVehicle = listVehicle.filter(generic_query)
    return listVehicle

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            Profile.objects.get_or_create(
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
        if user is not None:
            login(request, user)
            return redirect('index')
        else: 
            messages.error(request, "Invalid username or password.")
    
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def edit_profile(request):
    user = request.user
    manager = user.username=='admin'
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Redirect to the profile view after saving
    else:
        form = ProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form,'manager':manager})

def logout_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if not Favorite.objects.filter(profile=profile).exists():
        Favorite(profile=profile).save()
    favorite=Favorite.objects.get(profile=profile)
    favorite.favoritesCar.clear()
    favorite.favoritesMoto.clear()

    if "favoriteCarList" in request.session:
        for car_id in request.session["favoriteCarList"]:
            if Car.objects.filter(id=car_id).exists():
                car = Car.objects.get(id=car_id)
                favorite.favoritesCar.add(car)
    if "favoriteMotoList" in request.session:
        for moto_id in request.session["favoriteMotoList"]:
            moto = get_object_or_404(Moto, id=moto_id)
            favorite.favoritesMoto.add(moto)

    favorite.save()
    logout(request)
    return redirect('index') 

def index(request):
    cars = Car.objects.order_by('year')[:4]
    context = {'cars': cars,"manager":None}
    if request.user.is_authenticated:
        manager = request.user.username=='admin'
        if manager:
            #For Confirm Purchase
            listForAccept=[]
            form = ConfirmFilter(request.POST)
            print(request.POST)
            cars=Car.objects.all()
            motos=Moto.objects.all()
            filterProfile=False

            profiles = Profile.objects.exclude(user__username="admin")
            for car in cars:
                for profile in car.interestedCustomers.all():
                    if filterProfile and profile not in profiles:
                        continue
                    listForAccept.append({"vehicle":car,"profile":profile,"type":1})
            for moto in motos:
                for profile in moto.interestedCustomers.all():
                    if filterProfile and profile not in profiles:
                        continue
                    listForAccept.append({"vehicle":moto,"profile":profile,"type":0})
            context = {"listForAccept":listForAccept}
    return render(request, 'index.html', context)

def cars(request):
    carsList = Car.objects.all()
    form = CarSortAndFilter(request.POST or None)
    errors=None
    manager=None
    if request.user.is_authenticated:
        manager = request.user.username=='admin'
    if request.method == 'POST': 
        if form.is_valid():
            if form.cleaned_data['name']:
                carsList = filterByBrandAndName(form.cleaned_data['name'],carsList)
                
            if form.cleaned_data['isElectric']:
                carsList = carsList.filter(electric=True)
            if form.cleaned_data.get('priceMin') is not None:
                carsList = carsList.filter(price__gte=form.cleaned_data['priceMin'])
            if form.cleaned_data.get('priceMax') is not None:
                carsList = carsList.filter(price__lte=form.cleaned_data['priceMax'])
            if form.cleaned_data['numberDoors'] != "All":
                carsList = carsList.filter(doors=int(form.cleaned_data['numberDoors']))
            if form.cleaned_data['newOrUsed'] != "All":
                carsList = carsList.filter(new=form.cleaned_data['newOrUsed'] == "true")

            if form.cleaned_data['color'] != "None":
                carsList = carsList.filter(color__icontains=form.cleaned_data['color'])

            sort_option = form.cleaned_data['sort']
            if sort_option == "brand_asc":
                carsList = carsList.order_by('model__brand__name')
            elif sort_option == "brand_desc":
                carsList = carsList.order_by('-model__brand__name')
            elif sort_option == "price_asc":
                carsList = carsList.order_by('price')
            elif sort_option == "price_desc":
                carsList = carsList.order_by('-price')
            elif sort_option == "year_asc":
                carsList = carsList.order_by('year')
            elif sort_option == "year_desc":
                carsList = carsList.order_by('-year')
            elif sort_option == "kilometers_asc":
                carsList = carsList.order_by('kilometers')
            elif sort_option == "kilometers_desc":
                carsList = carsList.order_by('-kilometers')
        else:
            errors=form.errors.as_text()
    context = {"cars": carsList, "form": form,"manager":manager,"manager":manager,"errors":errors}
    return render(request, 'cars.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    isSelected = False
    isBuyed = None
    isFavorite = False
    isFavorite = False
    authenticated =False
    manager =False
    
    if request.user.is_authenticated:
        authenticated=True
        manager = request.user.username=='admin'
        profile = get_object_or_404(Profile, user=request.user)
        isSelected = car.interestedCustomers.filter(id=profile.id).exists()
        if car.purchaser is not None:
            isBuyed = car.purchaser.id == profile.id
        
        if Favorite.objects.filter(profile=profile).exists() and not "favoriteCarList" in request.session:
            # Load favorites to request.session
            request.session["favoriteCarList"] = [car.id for car in Favorite.objects.get(profile=profile).favoritesCar.all()]
        elif not "favoriteCarList" in request.session:
            request.session["favoriteCarList"] = []
        isFavorite = car_id in request.session["favoriteCarList"]
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
        "authenticated":authenticated,
        "manager":manager
    }
    return render(request, "car_detail.html", context)


def motorbike_detail(request, moto_id):
    moto = get_object_or_404(Moto, id=moto_id) 
    isSelected = False
    isBuyed = None
    isFavorite = False
    isFavorite = False
    authenticated =False
    manager =False
    
    if request.user.is_authenticated:
        authenticated=True
        manager = request.user.username=='admin'
        profile = get_object_or_404(Profile, user=request.user)
        isSelected = moto.interestedCustomers.filter(id=profile.id).exists()
        if moto.purchaser is not None:
            isBuyed = moto.purchaser.id == profile.id
        if Favorite.objects.filter(profile=profile).exists() and not "favoriteMotoList" in request.session:
            #Load favorites to request.session
            request.session["favoriteMotoList"] = [moto.id for moto in Favorite.objects.get(profile=profile).favoritesMoto.all()]
        elif not "favoriteMotoList" in request.session:
            request.session["favoriteMotoList"] = []
        isFavorite = moto_id in request.session["favoriteMotoList"]
    if request.POST:
        favoriteMotoList = request.session["favoriteMotoList"]
        if isFavorite:
            favoriteMotoList.remove(moto_id)
        else:
            favoriteMotoList.append(moto_id)
        
        request.session["favoriteMotoList"] = favoriteMotoList
        isFavorite = moto_id in request.session["favoriteMotoList"]

    context = {
        "moto": moto,
        "isSelected": isSelected,
        "isBuyed": isBuyed,
        "isFavorite": isFavorite,
        "authenticated":authenticated,
        "manager":manager
    }
    return render(request, 'motorbike_detail.html',context)

def selectCar(request, car_id):
    if not request.user.is_authenticated:
        return redirect("login")
    car = get_object_or_404(Car, id=car_id) 
    profile = get_object_or_404(Profile, user=request.user)

    if car.interestedCustomers.filter(id=profile.id).exists():
        car.interestedCustomers.remove(profile)
    else:
        car.interestedCustomers.add(profile)
    return redirect('car_detail', car_id=car.id)  

def selectMoto(request, moto_id):
    if not request.user.is_authenticated:
        return redirect("login")
    moto = get_object_or_404(Moto, id=moto_id) 
    profile = get_object_or_404(Profile, user=request.user) 

    if moto.interestedCustomers.filter(id=profile.id).exists():
        moto.interestedCustomers.remove(profile)
    else:
        moto.interestedCustomers.add(profile)
    return redirect('motorbike_detail', moto_id=moto.id) 

def approve(request, vehicle_id,profile_id,type):
    if type:
        vehicle = get_object_or_404(Car, id=vehicle_id) 
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id) 
    profile = get_object_or_404(Profile, id=profile_id) 

    vehicle.interestedCustomers.clear()  
    vehicle.purchaser=profile
    vehicle.save()
    
    return redirect('index')  

def negate(request, vehicle_id,profile_id,type):
    if type:
        vehicle = get_object_or_404(Car, id=vehicle_id) 
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id) 
    profile = get_object_or_404(Profile, id=profile_id) 

    vehicle.interestedCustomers.remove(profile)
    
    return redirect('index')  

def motorbikes(request):
    motosList=Moto.objects.all()
    form = MotoSortAndFilter(request.POST or None)
    errors=None
    manager=None
    if request.user.is_authenticated:
        manager = request.user.username=='admin'

    if request.method == 'POST': 
        if form.is_valid():
            if form.cleaned_data['name']:
                motosList = filterByBrandAndName(form.cleaned_data['name'],motosList)
                
            if form.cleaned_data.get('priceMin') is not None:
                motosList = motosList.filter(price__gte=form.cleaned_data['priceMin'])
            if form.cleaned_data.get('priceMax') is not None:
                motosList = motosList.filter(price__lte=form.cleaned_data['priceMax'])
            if form.cleaned_data['newOrUsed'] != "All":
                motosList = motosList.filter(new=form.cleaned_data['newOrUsed'] == "true")
            if form.cleaned_data['color'] != "None":
                motosList = motosList.filter(color__icontains=form.cleaned_data['color'])

            sort_option = form.cleaned_data['sort']
            if sort_option == "brand_asc":
                motosList = motosList.order_by('model__brand__name')
            elif sort_option == "brand_desc":
                motosList = motosList.order_by('-model__brand__name')
            elif sort_option == "price_asc":
                motosList = motosList.order_by('price')
            elif sort_option == "price_desc":
                motosList = motosList.order_by('-price')
            elif sort_option == "year_asc":
                motosList = motosList.order_by('year')
            elif sort_option == "year_desc":
                motosList = motosList.order_by('-year')
            elif sort_option == "kilometers_asc":
                motosList = motosList.order_by('kilometers')
            elif sort_option == "kilometers_desc":
                motosList = motosList.order_by('-kilometers')
        else:
            errors=form.errors.as_text()
    context = {"motos": motosList, "form": form,"manager":manager,"errors":errors}
    return render(request, 'motorbikes.html', context)


def brands(request):
    form = BrandSearchForm(request.GET)
    brands = Brand.objects.filter()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            brands = brands.filter(name__icontains=query)

    context = {
        'brands': brands,
    }
    return render(request, 'brands.html', context)

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    cars = Car.objects.filter(model__brand=brand)
    motos = Moto.objects.filter(model__brand=brand)
    context = {
        'brand': brand,
        'cars': cars,
        'motos': motos
    }
    return render(request, 'brand_detail.html', context)


def groups(request):
    form = GroupSearchForm(request.GET)
    groups = Group.objects.filter()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            groups = groups.filter(name__icontains=query)

    context = {
        'groups': groups,
    }
    return render(request, 'groups.html', context)

def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    brands = Brand.objects.filter(group=group)
    context = {'group': group, 'brands': brands}
    return render(request, 'group_detail.html', context)

def create_car_model(request,type):
    if request.method == 'POST':
        formModel = CreateCarModel(request.POST)
        
        if formModel.is_valid():
            brand=formModel.cleaned_data["brand"]
            name=formModel.cleaned_data["name"]
            base_price=formModel.cleaned_data["base_price"]
            specifications=formModel.cleaned_data["specifications"]
            releaseYear=formModel.cleaned_data["releaseYear"]
            CarModel.objects.create(
                brand=brand,
                name=name,
                base_price=base_price,
                specifications=specifications,
                releaseYear=releaseYear,
                vehicle_type="Car" if type else "Motorbike"
            ).save()
            if type:
                return redirect('createCar')
            else:
                return redirect('createMoto')
    else:
        formModel = CreateCarModel()
    return render(request, 'createCarModel.html', {'formModel': formModel,"type":type})

def createCar(request):
    errors=None
    if request.method == 'POST':
        form = CreateCar(request.POST, request.FILES)
        if form.is_valid():
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            kilometers = 0 if form.cleaned_data['kilometers'] is None else form.cleaned_data['kilometers']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            color = form.cleaned_data['color']
            doors = form.cleaned_data['doors']
            electric = form.cleaned_data['electric']
            new_car = Car(
                model=model,
                year=year,
                kilometers=kilometers,
                new=kilometers==0,
                price=price,
                image=image,
                color=color,
                doors=doors,
                electric=electric
            )
            new_car.save()
            print("Create CAR")
            return redirect("cars")
        else:
            errors=form.errors.as_text()
    else:
        form = CreateCar()

    context = {"form": form,"errors":errors}
    return render(request, 'createCar.html', context)

def updateCar(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = UpdateCar(request.POST, request.FILES)
        if form.is_valid():
            car.model = form.cleaned_data['model']
            car.year = form.cleaned_data['year']
            car.kilometers = form.cleaned_data['kilometers'] if form.cleaned_data['kilometers'] is not None else 0
            car.new=car.kilometers==0
            car.price = form.cleaned_data['price']
            car.color = form.cleaned_data['color']
            car.doors = form.cleaned_data['doors']
            car.electric = form.cleaned_data['electric']
            if form.cleaned_data['image']:
                car.image = form.cleaned_data['image'] 
            car.save()
            return redirect('car_detail', car_id=car.id) 

    else:
        form = UpdateCar(initial={
            'model': car.model,
            'year': car.year,
            'kilometers': car.kilometers,
            'price': car.price,
            'image': car.image,
            'color': car.color,
            'doors': car.doors,
            'electric': car.electric,
        })

    context = {'form': form, 'car': car}
    return render(request, 'updateCar.html', context)

def createMoto(request):
    errors=None
    if request.method == 'POST':
        form = CreateMoto(request.POST, request.FILES)
        if form.is_valid():
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            kilometers = 0 if form.cleaned_data['kilometers'] is None else form.cleaned_data['kilometers']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            color = form.cleaned_data['color']
            new_moto = Moto(
                model=model,
                year=year,
                kilometers=kilometers,
                new=kilometers==0,
                price=price,
                image=image,
                color=color,
            )
            new_moto.save()
            return redirect("motorbikes")
        else:
            errors=form.errors.as_text()
    else:
        form = CreateMoto()

    context = {"form": form,"errors": errors}
    return render(request, 'createMoto.html', context)

def updateMoto(request, moto_id):
    moto = get_object_or_404(Moto, id=moto_id)

    if request.method == 'POST':
        form = UpdateMoto(request.POST, request.FILES)
        if form.is_valid():
            moto.model = form.cleaned_data['model']
            moto.year = form.cleaned_data['year']
            moto.kilometers = form.cleaned_data['kilometers'] if form.cleaned_data['kilometers'] is not None else 0
            moto.new=moto.kilometers==0
            moto.price = form.cleaned_data['price']
            moto.color = form.cleaned_data['color']
            if form.cleaned_data['image']:
                moto.image = form.cleaned_data['image'] 
            moto.save()
            return redirect('motorbike_detail', moto_id=moto.id) 

    else:
        form = UpdateMoto(initial={
            'model': moto.model,
            'year': moto.year,
            'kilometers': moto.kilometers,
            'price': moto.price,
            'image': moto.image,
            'color': moto.color,
        })

    context = {'form': form, 'moto': moto}
    return render(request, 'updateMoto.html', context)


def deleteCar(request, car_id):
    car = get_object_or_404(Car, id=car_id) 
    car.delete()
    return redirect('cars')

def deleteMoto(request, moto_id):
    moto = get_object_or_404(Moto, id=moto_id) 
    moto.delete()
    return redirect('motorbikes')

def loadFavourites(request):
    if not request.user.is_authenticated:
        return redirect("login")
    profile = get_object_or_404(Profile, user=request.user)
    
    # Security measure for users who did not load their favorites in the vehicle details
    if Favorite.objects.filter(profile=profile).exists() and not "favoriteCarList" in request.session:
        request.session["favoriteCarList"] = [car.id for car in Favorite.objects.get(profile=profile).favoritesCar.all()]
    if Favorite.objects.filter(profile=profile).exists() and not "favoriteMotoList" in request.session:
        request.session["favoriteMotoList"] = [moto.id for moto in Favorite.objects.get(profile=profile).favoritesMoto.all()]
    if not "favoriteCarList" in request.session:
        request.session["favoriteCarList"] = []
    if not "favoriteMotoList" in request.session:
        request.session["favoriteMotoList"] = []

    context = {
        "favoriteCars": Car.objects.filter(id__in=request.session["favoriteCarList"]),
        "favoriteMotos": Moto.objects.filter(id__in=request.session["favoriteMotoList"])
    }

    return render(request, 'favourites.html', context)

def vehiclesPurchased(request):
    if not request.user.is_authenticated:
        return redirect("login")
    profile = get_object_or_404(Profile, user=request.user)
    cars = Car.objects.filter(purchaser=profile)
    motos = Moto.objects.filter(purchaser=profile)
    context = {
        "cars": cars,
        "motos": motos
    }
    return render(request, 'vehicles_purchased.html', context)

def desiredVehicles(request):
    if not request.user.is_authenticated:
        return redirect("login")
    profile = get_object_or_404(Profile, user=request.user)
    cars = Car.objects.filter(interestedCustomers=profile)
    motos = Moto.objects.filter(interestedCustomers=profile)
    context = {
        "cars": cars,
        "motos": motos
    }
    return render(request, 'desired_vehicles.html', context)


################# API #################
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.models import Profile, Group, Brand, CarModel, Car, Moto, Favorite
from app.serializers import (
    ProfileSerializer, GroupSerializer, BrandSerializer, 
    CarModelSerializer, CarSerializer, MotoSerializer, FavoriteSerializer,UserSerializer
)


################# Car #################

import random

@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    if 'num' in request.GET:
        num = int(request.GET['num'])
        cars = random.sample(list(cars), num)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_car(request):
    id = int(request.GET['id'])
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarSerializer(car)
    return Response(serializer.data)

import time
@api_view(['POST'])
def create_car(request):
    print("FILES:", request.FILES)
    print("DATA:", request.data)
    try:
        data = request.data.copy()

        model_id = data.get('model')
        year_str = data.get('year')
        price_str = data.get('price')

        try:
            model_instance = CarModel.objects.get(id=int(model_id))
        except (ValueError, CarModel.DoesNotExist):
            return Response({'error': f'CarModel with id {model_id} not found or invalid.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            year = int(year_str)
            print(year,time.localtime().tm_year)
            if model_instance.releaseYear>year or year>time.localtime().tm_year:
                return Response({'error': f'Year must be more than {model_instance.releaseYear} and not future.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({'error': 'Year must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)
  
        try:
            price = float(price_str)
            if 0>=price or int(price)>=1e8:
                return Response({'error': 'Ensure that there are no more than 8 digits before the decimal point.'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Price must be a valid decimal number.'}, status=status.HTTP_400_BAD_REQUEST)

        kilometers_str = data.get('kilometers', '0')
        if kilometers_str=="null" or kilometers_str=="":
            kilometers_str=0
        try:
            kilometers = float(kilometers_str)
        except ValueError:
            return Response({'error': 'Kilometers must be a float.'}, status=status.HTTP_400_BAD_REQUEST)
  
        color = data.get('color', 'Black')
        doors_str = data.get('doors', '4')
        try:
            doors = int(doors_str)
        except ValueError:
            return Response({'error': 'Doors must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

        electric_str = data.get('electric', 'false').lower()
        electric = (electric_str == 'true')

        if 'image' in request.FILES:
            image = data.get('image')

        new_car = Car(
            model=model_instance,
            year=year,
            kilometers=kilometers,
            new=(kilometers == 0),
            price=price,
            image=image,
            color=color,
            doors=doors,
            electric=electric
        )
        new_car.save()

        return Response(CarSerializer(new_car).data, status=status.HTTP_201_CREATED)
    except Exception as e:
            print("error:",e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_car(request):
    print(1)
    print(request.FILES)  
    print(request.data)   
    id = request.data.get('id')
    if not id:
        return Response({'error': 'ID not provided.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        car = Car.objects.get(id=id)
        oldModel=car.model
    except Car.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

    updatable_fields = {key: request.data[key] for key in ['model','id','year','kilometers','price','color','doors','electric','image'] if key in request.data}
    if 'image' in updatable_fields and not hasattr(updatable_fields['image'], 'read'):
        print(updatable_fields.pop('image'))

    kilometers_str = updatable_fields.get('kilometers', '0')
    if kilometers_str=="null" or kilometers_str=="":
        kilometers_str="0"
    updatable_fields["kilometers"] =kilometers_str
    updatable_fields["new"] =str(kilometers_str=="0")

    if 'model' in updatable_fields:
        model_id = updatable_fields.pop('model')  
        try:
            model_instance = CarModel.objects.get(id=model_id)
            car.model=model_instance  
            car.save()      
        except CarModel.DoesNotExist:
            return Response({'error': f'CarModel with id {model_id} not found.'}, status=status.HTTP_400_BAD_REQUEST)
    print(car.model)  

    year = int(updatable_fields.get('year', '0'))
    if model_instance.releaseYear>year or year>time.localtime().tm_year:
        return Response({'error': f'Year must be more than {model_instance.releaseYear} and not future.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CarSerializer(car, data=updatable_fields, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        car.model=oldModel  
        car.save()    
        print({"error":str(serializer.errors)})
    return Response({"error":str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_car(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
    
    car.delete()
    return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


################# Motorbike #################

@api_view(['GET'])
def get_motorbikes(request):
    motos = Moto.objects.all()
    if 'num' in request.GET:
        num = int(request.GET['num'])
        motos = random.sample(list(motos), num)
    serializer = MotoSerializer(motos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_motorbike(request):
    id = int(request.GET['id'])
    try:
        moto = Moto.objects.get(id=id)
    except Moto.DoesNotExist:
        return Response({'error': 'Motorbike not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = MotoSerializer(moto)
    return Response(serializer.data)


@api_view(['POST'])
def create_motorbike(request):
    print("FILES:", request.FILES)
    print("DATA:", request.data)

    data = request.data.copy()

    model_id = data.get('model')
    year_str = data.get('year')
    price_str = data.get('price')

    try:
        model_instance = CarModel.objects.get(id=int(model_id))
    except (ValueError, CarModel.DoesNotExist):
        return Response({'error': f'Motorbike model with id {model_id} not found or invalid.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        year = int(data.get('year', '0'))
        if model_instance.releaseYear>year or year>time.localtime().tm_year:
            return Response({'error': f'Year must be more than {model_instance.releaseYear} and not future.'}, status=status.HTTP_400_BAD_REQUEST)

    except ValueError:
        return Response({'error': 'Year must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        price = float(price_str)
        if 0>=price or int(price)>=1e8:
            return Response({'error': 'Ensure that there are no more than 8 digits before the decimal point.'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error': 'Price must be a valid decimal number.'}, status=status.HTTP_400_BAD_REQUEST)


    kilometers_str = data.get('kilometers', '0')
    if kilometers_str == "null" or kilometers_str == "":
        kilometers_str = 0
    print(kilometers_str)
    try:
        kilometers = float(kilometers_str)
    except ValueError:
        return Response({'error': 'Kilometers must be a float.'}, status=status.HTTP_400_BAD_REQUEST)

    color = data.get('color', 'Black')

    image = None
    if 'image' in request.FILES:
        image = data.get('image')

    new_motorbike = Moto(
        model=model_instance,
        year=year,
        kilometers=kilometers,
        new=(kilometers == 0),
        price=price,
        image=image,
        color=color,
    )
    new_motorbike.save()
    return Response(MotoSerializer(new_motorbike).data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_motorbike(request):
    id = request.data['id']
    print(request.data)
    try:
        moto = Moto.objects.get(id=id)
        oldModel=moto.model
    except Moto.DoesNotExist:
        return Response({'error': 'Motorbike not found'}, status=status.HTTP_404_NOT_FOUND)
    
    updatable_fields = {key: request.data[key] for key in ['id','model','year','kilometers','price','color','image'] if key in request.data}

    kilometers_str = updatable_fields.get('kilometers', '0')
    if kilometers_str=="null" or kilometers_str=="":
        kilometers_str="0"
    updatable_fields["kilometers"] =kilometers_str
    updatable_fields["new"] =str(kilometers_str=="0")

    if 'image' in updatable_fields and not hasattr(updatable_fields['image'], 'read'):
        print(updatable_fields.pop('image'))
    if 'model' in updatable_fields:
        model_id = updatable_fields.pop('model')
        try:
            model_instance = CarModel.objects.get(id=model_id)
            moto.model=model_instance  
            moto.save()      
        except CarModel.DoesNotExist:
            return Response({'error': f'CarModel with id {model_id} not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
    year = int(updatable_fields.get('year', '0'))
    if model_instance.releaseYear>year or year>time.localtime().tm_year:
        return Response({'error': f'Year must be more than {model_instance.releaseYear} and not future.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = CarSerializer(moto, data=updatable_fields, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else: 
        moto.model=oldModel  
        moto.save()    
        print({"error":str(serializer.errors)})
    return Response({"error":str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_motorbike(request, id):
    try:
        moto = Moto.objects.get(id=id)
    except Moto.DoesNotExist:
        return Response({'error': 'Motorbike not found'}, status=status.HTTP_404_NOT_FOUND)
    
    moto.delete()
    return Response({'message': 'Motorbike deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


################# Groups #################

@api_view(['GET'])
def get_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_group(request):
    id = int(request.GET['id'])
    try:
        group = Group.objects.get(id=id)
    except Group.DoesNotExist:
        return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = GroupSerializer(group)
    return Response(serializer.data)

@api_view(['GET'])
def get_brands_by_group(request, id):
    try:
        brand = Brand.objects.get(id=id)
    except Brand.DoesNotExist:
        return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)
    
    cars = Car.objects.filter(model__brand=brand)
    motos = Moto.objects.filter(model__brand=brand)
    
    car_serializer = CarSerializer(cars, many=True)
    moto_serializer = MotoSerializer(motos, many=True)
    
    return Response({
        'cars': car_serializer.data,
        'motos': moto_serializer.data
    })


################# Brands #################

@api_view(['GET'])
def get_brands(request):
    brands = Brand.objects.prefetch_related(
        'models__cars',
        'models__motos'
    ).all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_brand(request):
    id = int(request.GET['id'])
    try:
        brand = Brand.objects.get(id=id)
    except Brand.DoesNotExist:
        return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BrandSerializer(brand)
    return Response(serializer.data)

@api_view(['GET'])
def get_models_by_type(request, vehicle_type):
    if vehicle_type not in ['Car', 'Motorbike']:
        return Response({"error": "Invalid vehicle type."}, status=status.HTTP_400_BAD_REQUEST)
    models = CarModel.objects.filter(vehicle_type=vehicle_type)
    serializer = CarModelSerializer(models, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_models_by_brand(request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        cars = Car.objects.filter(model__brand=brand)
        motos = Moto.objects.filter(model__brand=brand)

        car_serializer = CarSerializer(cars, many=True)
        moto_serializer = MotoSerializer(motos, many=True)

        return Response({
            'brand': brand.name,
            'cars': car_serializer.data,
            'motos': moto_serializer.data
        })
    except Brand.DoesNotExist:
        return Response({'error': 'Brand not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_models_by_type(request, vehicle_type):
    if vehicle_type not in ['Car', 'Motorbike']:
        return Response({"error": "Invalid vehicle type."}, status=status.HTTP_400_BAD_REQUEST)

    models = CarModel.objects.filter(vehicle_type=vehicle_type)
    serializer = CarModelSerializer(models, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

################# Search #################

@api_view(['GET'])
def search(request, type):
    query = request.GET.get('q', '').strip()
    if query:
        search_terms = query.split()

        if type == 'brands':
            brands = Brand.objects.filter(name__icontains=query)
            serializer = BrandSerializer(brands, many=True)
            return Response(serializer.data)

        if type == 'groups':
            groups = Group.objects.filter(name__icontains=query)
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data)

        if type in ['cars', 'motos']:
            if type == 'cars':
                model_class = Car
                serializer_class = CarSerializer
            else:
                model_class = Moto
                serializer_class = MotoSerializer

            name_query = Q()
            match_found = False
            list_vehicle = model_class.objects.all()

            for i in range(len(search_terms), 0, -1):
                possible_brand = " ".join(search_terms[:i])
                remaining_terms = search_terms[i:]

                brand_query = Q(model__brand__name__icontains=possible_brand)
                model_query = Q()

                for term in remaining_terms:
                    model_query &= Q(model__name__icontains=term)

                if remaining_terms:
                    name_query = brand_query & model_query
                else:
                    name_query = brand_query | Q(model__name__icontains=possible_brand)

                if list_vehicle.filter(name_query).exists():
                    match_found = True
                    list_vehicle = list_vehicle.filter(name_query)
                    break

            if not match_found:
                generic_query = Q()
                for term in search_terms:
                    generic_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
                list_vehicle = list_vehicle.filter(generic_query)

            serializer = serializer_class(list_vehicle, many=True)
            return Response(serializer.data)

    return Response({'error': 'No results found'}, status=status.HTTP_404_NOT_FOUND)


################# Filters #################

# Search for vehicles, brands, or groups with filters and sorting.
@api_view(['GET'])
def unified_search_and_filter(request, type):
    query = request.GET.get('q', '').strip()
    filters = {
        'minPrice': request.GET.get('minPrice'),
        'maxPrice': request.GET.get('maxPrice'),
        'color': request.GET.get('color'),
        'isEletric': request.GET.get('isEletric'),
        'doors': request.GET.get('doors'),
        'condition': request.GET.get('condition')
    }
    sort_option = request.GET.get('sort')

    if type == 'brands':
        brands = Brand.objects.filter(name__icontains=query) if query else Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)

    if type == 'groups':
        groups = Group.objects.filter(name__icontains=query) if query else Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    if type in ['cars', 'motos']:
        model_class = Car if type == 'cars' else Moto
        serializer_class = CarSerializer if type == 'cars' else MotoSerializer

        objects = model_class.objects.all()
        if query:
            objects=filterByBrandAndName(query,objects)

        if filters['minPrice']:
            objects = objects.filter(price__gte=filters['minPrice'])
        if filters['maxPrice']:
            objects = objects.filter(price__lte=filters['maxPrice'])
        if filters['color'] != "" and filters['color'] != None:
            objects = objects.filter(color__icontains=filters['color'])
        if filters['isEletric']:
            objects = objects.filter(electric=(filters['isEletric'].lower() == 'true'))
        if filters['doors']:
            objects = objects.filter(doors=int(filters['doors']))
        if filters['condition'] != "" and filters['condition'] != None:
            objects = objects.filter(new=filters['condition'].lower() == 'new')

        if sort_option:
            sort_fields = {
                'price_asc': 'price',
                'price_desc': '-price',
                'year_asc': 'year',
                'year_desc': '-year',
                'kilometers_asc': 'kilometers',
                'kilometers_desc': '-kilometers',
            }
            if sort_option in sort_fields:
                objects = objects.order_by(sort_fields[sort_option])

        serializer = serializer_class(objects, many=True)
        return Response(serializer.data)

    return Response({'error': 'Invalid type or no results found'}, status=status.HTTP_404_NOT_FOUND)

################# Authentication #################
from django.core.cache import cache
def getUniqueID(request):
        print(request.headers["User-Agent"])
        ID=str((request.headers["User-Agent"]))
        print("ID:",ID)
        return ID
        return "user"

@api_view(['POST'])
def post_sign_up(request):
    data = request.data
    serializer = UserSerializer(data=data)
    print(serializer)
    if serializer.is_valid():
        user = serializer.save()
        user.refresh_from_db()
        print(user)
        login(request, user)
        cache.set(getUniqueID(request),user,timeout=10800)
        return Response({"message": "User created and logged in successfully."}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_log_in(request):
    print(request.user)
    username = request.data.get('username')
    password = request.data.get('password')
    print(request.data)
    print([(user1.user.username,user1.user.password) for user1 in Profile.objects.all()])
    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        cache.set(getUniqueID(request),user,timeout=10800)
        print(cache.get(getUniqueID(request)))
        print(cache.get(getUniqueID(request)))
        return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def post_logout_view(request):
    user = cache.get(getUniqueID(request))
    print(user)
    logout(request)
    cache.delete(getUniqueID(request))
    return Response({"message": "Logged out and favorites saved."}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_isAuth(request):
    user = cache.get(getUniqueID(request))
    print(user)
    if user is None:
        data = {"authenticated": False, "isManager": False, "username": "", "favoriteCarList":[], "favoriteMotoList":[]}
    else:
        favoriteCarList=[]
        favoriteMotoList=[]
        profile = get_object_or_404(Profile, user=user)
        if Favorite.objects.filter(profile=profile).exists():
            favoriteCarList = [car.id for car in Favorite.objects.get(profile=profile).favoritesCar.all()]
        if Favorite.objects.filter(profile=profile).exists():
            favoriteMotoList = [moto.id for moto in Favorite.objects.get(profile=profile).favoritesMoto.all()]
        data = {"authenticated": True, "isManager": user.username == "admin", "username": user.username, "favoriteCarList":favoriteCarList, "favoriteMotoList":favoriteMotoList}
    return Response(data)

from django.http import JsonResponse

@api_view(['POST'])
def save_favorites(request, type):
    user = cache.get(getUniqueID(request))
    if not user:
        return Response({"error": "User not authenticated."}, status=401)
    
    profile = get_object_or_404(Profile, user=user)
    favorite, created = Favorite.objects.get_or_create(profile=profile)
    
    if type == "cars":
        favorite.favoritesCar.clear()
    elif type == "motos":
        favorite.favoritesMoto.clear()

    favorites = request.data.get("favorites", [])
    if type == "cars":
        for car_id in favorites:
            car = Car.objects.filter(id=car_id).first()
            if car:
                favorite.favoritesCar.add(car)
    elif type == "motos":
        for moto_id in favorites:
            moto = Moto.objects.filter(id=moto_id).first()
            if moto:
                favorite.favoritesMoto.add(moto)

    favorite.save()

    return Response({"message": f"{type.capitalize()} favorites updated successfully."})


@api_view(['GET'])
def get_favorites(request, type):
    user = cache.get(getUniqueID(request))
    if not user:
        return Response({"error": "User not authenticated."}, status=401)
    
    favorites_ids = request.GET.getlist('favorites')
    print(favorites_ids)
    if type == "cars":
        favorites = Car.objects.filter(id__in=favorites_ids)
        serialized_favorites = CarSerializer(favorites, many=True).data
    elif type == "motos":
        favorites = Moto.objects.filter(id__in=favorites_ids)
        serialized_favorites = MotoSerializer(favorites, many=True).data
    else:
        return Response({"error": "Invalid type specified."}, status=400)
    
    return Response({
        "message": f"Fetched {type} favorites successfully.",
        "favorites": serialized_favorites
    })


@api_view(['GET'])
def get_vehicle_status(request, vehicle_id, type):
    user = cache.get(getUniqueID(request))
    if user is None:
        return Response({
        "isSelected": False
    })

    if not user.is_authenticated:
        return Response({"error": "User not authenticated."}, status=401)

    profile = get_object_or_404(Profile, user=user)
    isBuyed=None
    if type == "car":
        vehicle = get_object_or_404(Car, id=vehicle_id)
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id)

    isSelected = vehicle.interestedCustomers.filter(id=profile.id).exists()
    if vehicle.purchaser:
        isBuyed = vehicle.purchaser.id == profile.id if vehicle.purchaser else False
    print({"isSelected": isSelected,"isBuyed": isBuyed,})
    return Response({
        "isSelected": isSelected,
        "isBuyed": isBuyed,
    })


@api_view(['POST'])
def toggle_interest(request, vehicle_id, type):
    user = cache.get(getUniqueID(request))
    if not user.is_authenticated:
        return Response({"error": "User not authenticated."}, status=401)

    profile = get_object_or_404(Profile, user=user)
    print(user,profile)
    if type == "car":
        vehicle = get_object_or_404(Car, id=vehicle_id)
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id)


    if vehicle.interestedCustomers.filter(id=profile.id).exists():
        vehicle.interestedCustomers.remove(profile)
    else:
        vehicle.interestedCustomers.add(profile)
    isSelected = vehicle.interestedCustomers.filter(id=profile.id).exists()
    print("isSelected",isSelected)
    return Response({"message": f"Interest {isSelected} successfully."})


@api_view(['GET'])
def get_vehicles_for_approval(request):

    query_vehicle = request.GET.get('qVehicle', '').strip()
    query_user = request.GET.get('qUser', '').strip()

    cars = Car.objects.all()
    motos = Moto.objects.all()

    if query_vehicle:
        cars = filterByBrandAndName(query_vehicle,cars)
        motos = filterByBrandAndName(query_vehicle,motos)

    profiles = Profile.objects.exclude(user__username="admin")

    if query_user:
        profiles = profiles.filter(Q(user__username__icontains=query_user))

    listForAccept = []

    for car in cars:
        for profile in car.interestedCustomers.all():
            if profile not in profiles:
                continue
            listForAccept.append({
                "vehicle": CarSerializer(car).data,
                "profile": ProfileSerializer(profile).data,
                "type": "cars"
            })

    for moto in motos:
        for profile in moto.interestedCustomers.all():
            if profile not in profiles:
                continue
            listForAccept.append({
                "vehicle": MotoSerializer(moto).data,
                "profile": ProfileSerializer(profile).data,
                "type": "moto"
            })

    return Response({"listForAccept": listForAccept}, status=status.HTTP_200_OK)


@api_view(['POST'])
def approve_customer(request, vehicle_id, profile_id, type):
    user = cache.get(getUniqueID(request))
    if not user or not user.is_authenticated or not user.username=='admin':
        return Response({"error": "User not authenticated or Not is The Manager."}, status=401)
        return Response({"error": "User not authenticated or Not is The Manager."}, status=401)
    if type == "cars":
        vehicle = get_object_or_404(Car, id=vehicle_id)
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id)

    profile = get_object_or_404(Profile, id=profile_id)

    vehicle.interestedCustomers.clear()
    vehicle.purchaser = profile
    vehicle.save()

    return Response({"message": "Customer approved and assigned to vehicle."})


@api_view(['POST'])
def negate_customer(request, vehicle_id, profile_id, type):
    user = cache.get(getUniqueID(request))
    if not user or not user.is_authenticated or not user.username=='admin':
        return Response({"error": "User not authenticated or Not is The Manager."}, status=401)
    if type == "cars":
        vehicle = get_object_or_404(Car, id=vehicle_id)
    else:
        vehicle = get_object_or_404(Moto, id=vehicle_id)


    profile = get_object_or_404(Profile, id=profile_id)

    vehicle.interestedCustomers.remove(profile)

    return Response({"message": "Customer removed from interested list."})

@api_view(['POST'])
def create_car_model(request):
    brand_id = request.data.get('brand')
    name = request.data.get('name')
    base_price_str = request.data.get('base_price')
    specifications = request.data.get('specifications')
    release_year_str = request.data.get('releaseYear')
    vehicle_type = request.data.get('vehicle_type', 'Car')

    try:
        brand = Brand.objects.get(id=int(brand_id))
    except (ValueError, Brand.DoesNotExist):
        return Response({'error': f'Brand with id {brand_id} not found.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        base_price = float(base_price_str)
    except ValueError:
        return Response({'error': 'base_price must be a float.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        release_year = int(release_year_str)
        if release_year < 1990 or release_year > 2024:
            return Response({'error': 'releaseYear must be between 1990 and 2024.'}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({'error': 'releaseYear must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

    new_model = CarModel(
        brand=brand,
        name=name,
        base_price=base_price,
        specifications=specifications,
        releaseYear=release_year,
        vehicle_type=vehicle_type
    )

    new_model.save()

    return Response(CarModelSerializer(new_model).data, status=status.HTTP_201_CREATED)

################# Profile #################

@api_view(['GET', 'PUT'])
def get_profile(request):
    user = cache.get(getUniqueID(request))
    if not user or not user.is_authenticated:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        profile = Profile.objects.get(user=user)
        user_obj = User.objects.get(id=user.id)

        if request.method == 'GET':
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=200)
                    
        elif request.method == 'PUT':
            print(request.data)
            data = request.data.copy()
            user_data = data.pop('user', None)
            profile_serializer = ProfileSerializer(profile, data=data, partial=True)
            print("profile_serializer",profile_serializer)
            user_data['first_name']=data['first_name']
            user_data['last_name']=data['last_name']
            user_data['email']=data['email']
            print("user_data",user_data)
            user_serializer = None
            if user_data:
                user_serializer = UserSerializer(user_obj, data=user_data, partial=True)

            print("user_serializer",user_serializer)
            print()
            if profile_serializer.is_valid() and  user_serializer.is_valid():
                profile_serializer.save()
                user_serializer.save()

                updated_profile_serializer = ProfileSerializer(profile)
                return Response(updated_profile_serializer.data, status=status.HTTP_200_OK)

            print(serializer.errors)
            print("UU", user_serializer.errors)
            errors = profile_serializer.errors
            if user_serializer and user_serializer.errors:
                errors['user'] = user_serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    except Profile.DoesNotExist:
        return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_purchased_vehicles(request):
    user = cache.get(getUniqueID(request))
    if not user or not user.is_authenticated:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    profile = get_object_or_404(Profile, user=user)
    cars = Car.objects.filter(purchaser=profile)
    motos = Moto.objects.filter(purchaser=profile)

    car_serializer = CarSerializer(cars, many=True)
    moto_serializer = MotoSerializer(motos, many=True)

    return Response({
        'cars': car_serializer.data,
        'motos': moto_serializer.data
    })

@api_view(['GET'])
def get_desired_vehicles(request):
    user = cache.get(getUniqueID(request))
    if not user or not user.is_authenticated:
        return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    profile = get_object_or_404(Profile, user=user)
    cars = Car.objects.filter(interestedCustomers=profile)
    motos = Moto.objects.filter(interestedCustomers=profile)

    car_serializer = CarSerializer(cars, many=True)
    moto_serializer = MotoSerializer(motos, many=True)

    return Response({
        'cars': car_serializer.data,
        'motos': moto_serializer.data
    })

