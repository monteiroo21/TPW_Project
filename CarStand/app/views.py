from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from app.forms import SignUpForm, LoginForm, GroupSearchForm, BrandSearchForm,CarSortAndFilter
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

# def cars(request):
#     #creategroups()
#     carsList=Car.objects.all()
#     form = CarSortAndFilter(request.POST)

#     if request.method == 'POST' and form.is_valid():
#         if form.cleaned_data['name']:
#             # carsList = carsList.filter(model__name__icontains=form.cleaned_data['name'])
#             carsList = carsList.filter(
#                 Q(model__name__icontains=form.cleaned_data['name']) | Q(model__brand__name__icontains=form.cleaned_data['name'])
#             )
        
#         if form.cleaned_data['isElectric']:
#             carsList = carsList.filter(electric=True)
#         if form.cleaned_data.get('priceMin'):
#             carsList = carsList.filter(price__gte=form.cleaned_data['priceMin'])
#         if form.cleaned_data.get('priceMax'):
#             carsList = carsList.filter(price__lte=form.cleaned_data['priceMax'])
#         if form.cleaned_data['numberDoors']!="All":
#             carsList = carsList.filter(doors=int(form.cleaned_data['numberDoors']))
#         if form.cleaned_data['newOrUsed']!="All":
#             carsList = carsList.filter(new=form.cleaned_data['newOrUsed']=="true")

#         if form.cleaned_data['color']!="None":
#             carsList = carsList.filter(color__icontains=form.cleaned_data['color'])

#         sort_option = form.cleaned_data['sort']
#         if sort_option == "1":
#             carsList = carsList.order_by('model__name')
#         elif sort_option == "2":
#             carsList = carsList.order_by('price')
#         elif sort_option == "3":
#             carsList = carsList.order_by('year')
#     context = {"cars":carsList,"form":form}
#     form = CarSortAndFilter(request.POST)

#     if request.method == 'POST' and form.is_valid():
#         if form.cleaned_data['name']:
#             carsList = carsList.filter(model__name__icontains=form.cleaned_data['name'])
        
#         if form.cleaned_data['isElectric']:
#             carsList = carsList.filter(electric=True)
#         if form.cleaned_data.get('priceMin'):
#             carsList = carsList.filter(price__gte=form.cleaned_data['priceMin'])
#         if form.cleaned_data.get('priceMax'):
#             carsList = carsList.filter(price__lte=form.cleaned_data['priceMax'])
#         if form.cleaned_data['numberDoors']!="All":
#             carsList = carsList.filter(doors=int(form.cleaned_data['numberDoors']))
#         if form.cleaned_data['newOrUsed']!="All":
#             carsList = carsList.filter(new=form.cleaned_data['newOrUsed']=="true")

#         if form.cleaned_data['color']!="None":
#             carsList = carsList.filter(color__icontains=form.cleaned_data['color'])

#         sort_option = form.cleaned_data['sort']
#         if sort_option == "1":
#             carsList = carsList.order_by('model__brand__name')
#         elif sort_option == "2":
#             carsList = carsList.order_by('price')
#         elif sort_option == "3":
#             carsList = carsList.order_by('year')

#     context = {"cars": carsList,"form": form}
#     return render(request, 'cars.html', context)


def cars(request):
    carsList = Car.objects.all()
    form = CarSortAndFilter(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        if form.cleaned_data['name']:
            # search_terms = form.cleaned_data['name'].split()
            # name_query = Q()
            # for term in search_terms:
            #     name_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
            # carsList = carsList.filter(name_query)
            # search_terms = form.cleaned_data['name'].split()
            # name_query = Q()

            # first_term = search_terms[0]
            # remaining_terms = search_terms[1:]
            
            # brand_query = Q(model__brand__name__icontains=first_term)
            # model_query = Q()
            # for term in remaining_terms:
            #     model_query &= Q(model__name__icontains=term)
            
            # if remaining_terms:
            #     name_query = brand_query & model_query
            # else:
            #     name_query = Q(model__name__icontains=first_term) | Q(model__brand__name__icontains=first_term)
            
            # carsList = carsList.filter(name_query)
            search_terms = form.cleaned_data['name'].split()
            name_query = Q()
            match_found = False
            
            # Iterar sobre cada possível divisão de termos em marca e modelo
            for i in range(len(search_terms), 0, -1):
                possible_brand = " ".join(search_terms[:i])
                remaining_terms = search_terms[i:]

                # Verificar se existe uma marca que corresponde aos termos possíveis
                brand_query = Q(model__brand__name__icontains=possible_brand)
                model_query = Q()

                # Aplicar filtro no modelo usando os termos restantes
                for term in remaining_terms:
                    model_query &= Q(model__name__icontains=term)

                # Marca e modelo correspondem
                if remaining_terms:
                    name_query = brand_query & model_query
                else:
                    # Apenas a marca corresponde
                    name_query = brand_query | Q(model__name__icontains=possible_brand)
                
                # Testar se o filtro retorna algum resultado
                if carsList.filter(name_query).exists():
                    match_found = True
                    carsList = carsList.filter(name_query)
                    break

            # Se não encontrou nenhuma correspondência com marca + modelo, aplicar pesquisa genérica
            if not match_found:
                generic_query = Q()
                for term in search_terms:
                    generic_query |= Q(model__name__icontains=term) | Q(model__brand__name__icontains=term)
                carsList = carsList.filter(generic_query)
        
        # Filtrar por outros campos
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

        # Ordenação
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
    
    if "favoriteCarList" not in request.session:
        request.session["favoriteCarList"] = []
    
    isFavorite = car_id in request.session["favoriteCarList"]
    
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        isSelected = car.interestedCustomers.filter(id=profile.id).exists()
        if car.purchaser is not None:
            isBuyed = car.purchaser.id == profile.id
    
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
    context = {"motos":motosList}
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

def get_5cars(request):
    cars = CarModel.objects.filter()[0:4]
    context = {'cars': cars}
    return render(request, 'index.html', context)

    