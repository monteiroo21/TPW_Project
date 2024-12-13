"""
URL configuration for CarStand project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    path('', RedirectView.as_view(url='index/', permanent=True), name='index'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),  
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('index/', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('createCar/', views.createCar, name='createCar'),
    path('updateCar/<int:car_id>/', views.updateCar, name='updateCar'),
    path('deleteCar/<int:car_id>/', views.deleteCar, name='deleteCar'),
    path('selectCar/<int:car_id>/', views.selectCar, name='selectCar'),
    path('createMoto/', views.createMoto, name='createMoto'),
    path('updateMoto/<int:moto_id>/', views.updateMoto, name='updateMoto'),
    path('deleteMoto/<int:moto_id>/', views.deleteMoto, name='deleteMoto'),
    path('selectMoto/<int:moto_id>/', views.selectMoto, name='selectMoto'),
    path('approve/<int:vehicle_id>/<int:profile_id>/<int:type>/', views.approve, name='approve'),
    path('negate/<int:vehicle_id>/<int:profile_id>/<int:type>/', views.negate, name='negate'),
    path('motorbikes/', views.motorbikes, name='motorbikes'),
    path('brands/', views.brands, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('motorbike/<int:moto_id>/', views.motorbike_detail, name='motorbike_detail'),
    path('favourites/', views.loadFavourites, name='favourites'),
    path('vehiclespurchased/', views.vehiclesPurchased, name='vehiclespurchased'),
    path('create-car-model/<int:type>', views.create_car_model, name='create_car_model'),
    path('vehiclespurchased/', views.vehiclesPurchased, name='vehiclespurchased'),
    path('desiredvehicles/', views.desiredVehicles, name='desiredvehicles'),

    ############################## API ##############################
    path('api/cars', views.get_cars, name='api_get_cars'),
    path('api/car', views.get_car, name='api_get_car'),
    path('api/cars/create', views.create_car, name='api_create_car'),
    path('api/cars/update', views.update_car, name='api_update_car'),
    path('api/cars/delete/<int:id>', views.delete_car, name='api_delete_car'),
    path('api/motos', views.get_motorbikes, name='api_get_motorbikes'),
    path('api/moto', views.get_motorbike, name='api_get_motorbike'),
    path('api/motos/create', views.create_motorbike, name='api_create_motorbike'),
    path('api/motos/update', views.update_motorbike, name='api_update_motorbike'),
    path('api/motos/delete/<int:id>', views.delete_motorbike, name='api_delete_motorbike'),
    path('api/brands', views.get_brands, name='api_get_brands'),
    path('api/brand', views.get_brand, name='api_get_brand'),
    path('api/groups', views.get_groups, name='api_get_groups'),
    path('api/group', views.get_group, name='api_get_group'),
    path('api/search/<str:type>/', views.search, name='search'),
    path('api/signup', views.post_sign_up, name='api_post_sign_up'),
    path('api/login', views.post_log_in, name='api_post_log_in'),
    path('api/logout', views.post_logout_view, name='api_post_logout_view'),
    path('api/isAuth', views.get_isAuth, name='api_get_isAuth'),
    path('api/favorites/<str:type>/', views.save_favorites, name='api_save_favorites'),
]

# Serve static files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
