from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from app.forms import ConfirmFilter, CreateMoto, MotoSortAndFilter, SignUpForm, LoginForm, GroupSearchForm, BrandSearchForm,CarSortAndFilter,CreateCar,CreateCarModel, UpdateCar, ProfileForm, UpdateMoto
from django.contrib.auth import login, authenticate, logout
from .models import Group, Brand, Profile,Favorite
from django.db.models import Q
from app.loadBackup import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            listForAccept=[]
            form = ConfirmFilter(request.POST)
            print(request.POST)
            cars=Car.objects.all()
            motos=Moto.objects.all()
            filterProfile=False

            if request.method == 'POST': 
                if form.is_valid():
                    if 'name' in form.cleaned_data:
                        cars = filterByBrandAndName(form.cleaned_data['name'],cars)
                        motos = filterByBrandAndName(form.cleaned_data['name'],motos)

                
                    if form.cleaned_data['typeV'] != "None":
                        if form.cleaned_data['typeV']=="Car":
                            motos = motos.filter(id=-1)
                        else:
                            cars = cars.filter(id=-1)
                    if form.cleaned_data['profile'] is not None:
                        filterProfile=True
                        profileName=form.cleaned_data['profile']
                        profiles = Profile.objects.exclude(user__username="admin").filter(user__username__icontains=profileName)
                        

                else:   
                    form = ConfirmFilter() 
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
            context = {"listForAccept":listForAccept,"form":form,"manager":manager}
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
