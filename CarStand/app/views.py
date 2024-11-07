from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from app.forms import MotoSortAndFilter, SignUpForm, LoginForm, GroupSearchForm, BrandSearchForm,CarSortAndFilter,CreateCar
from django.contrib.auth import login, authenticate, logout
from .models import Group, Brand, Profile,Favorite
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
    profile = get_object_or_404(Profile, user=request.user)
    if not Favorite.objects.filter(profile=profile).exists():
        Favorite(profile=profile).save()
    favorite=Favorite.objects.get(profile=profile)
    favorite.favoritesCar.clear()
    favorite.favoritesMoto.clear()

    if "favoriteCarList" in request.session:
        for car_id in request.session["favoriteCarList"]:
            car = get_object_or_404(Car, id=car_id)
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
    for k,v in request.session.items():
        print(k,v)
    context = {'cars': cars}
    return render(request, 'index.html', context)

def cars(request):
    carsList = Car.objects.all()
    form = CarSortAndFilter(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['name']:
            search_terms = form.cleaned_data['name'].split()
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
                
                if carsList.filter(name_query).exists():
                    match_found = True
                    carsList = carsList.filter(name_query)
                    break

            if not match_found:
                generic_query = Q()
                for term in search_terms:
                    generic_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
                carsList = carsList.filter(generic_query)
        
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
        if sort_option == "1":
            carsList = carsList.order_by('model__brand__name')
        elif sort_option == "2":
            carsList = carsList.order_by('price')
        elif sort_option == "3":
            carsList = carsList.order_by('year')

    context = {"cars": carsList, "form": form}
    return render(request, 'cars.html', context)


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    isSelected = False
    isBuyed = None
    isFavorite = False

    
    
    if request.user.is_authenticated:
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
    if car.interestedCustomers.filter(id=profile.id).exists():
        car.interestedCustomers.remove(profile)
    else:
        car.interestedCustomers.add(profile)

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
    form = MotoSortAndFilter(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['name']:
            search_terms = form.cleaned_data['name'].split()
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
                
                if motosList.filter(name_query).exists():
                    match_found = True
                    motosList = motosList.filter(name_query)
                    break

            if not match_found:
                generic_query = Q()
                for term in search_terms:
                    generic_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
                motosList = motosList.filter(generic_query)
        

        if form.cleaned_data.get('priceMin') is not None:
            motosList = motosList.filter(price__gte=form.cleaned_data['priceMin'])
        if form.cleaned_data.get('priceMax') is not None:
            motosList = motosList.filter(price__lte=form.cleaned_data['priceMax'])
        if form.cleaned_data['newOrUsed'] != "All":
            motosList = motosList.filter(new=form.cleaned_data['newOrUsed'] == "true")
        if form.cleaned_data['color'] != "None":
            motosList = motosList.filter(color__icontains=form.cleaned_data['color'])

        sort_option = form.cleaned_data['sort']
        if sort_option == "1":
            motosList = motosList.order_by('model__brand__name')
        elif sort_option == "2":
            motosList = motosList.order_by('price')
        elif sort_option == "3":
            motosList = motosList.order_by('year')

    context = {"motos": motosList, "form": form}
    return render(request, 'motorbikes.html', context)

# def brands(request):
#     groups = Group.objects.prefetch_related('brands')
#     context = {'groups': groups}
#     return render(request, 'brands.html', context)

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

def createCar(request):
    if request.method == 'POST':
        form = CreateCar(request.POST, request.FILES)  # Certifique-se de incluir request.FILES
        if form.is_valid():
            # Dados do formulário processados
            model = form.cleaned_data['model']
            year = form.cleaned_data['year']
            kilometers =0 if not 'kilometers' in   form.cleaned_data else form.cleaned_data['kilometers']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            color = form.cleaned_data['color']
            doors = form.cleaned_data['doors']
            electric = form.cleaned_data['electric']
            print(image)
            # Criação do novo carro
            new_car = Car(
                model=model,
                year=year,
                kilometers=kilometers,
                price=price,
                image=image,
                color=color,
                doors=doors,
                electric=electric
            )
            new_car.save()
            print("Create CAR")
            # Redireciona após salvar
            return redirect("cars")
        print(form.errors)  # Exibe os erros para depuração
    else:
        form = CreateCar()

    context = {"form": form}
    return render(request, 'createCar.html', context)