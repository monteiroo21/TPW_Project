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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    path('', RedirectView.as_view(url='index/', permanent=True), name='index'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('selectCar/<int:car_id>/', views.selectCar, name='selectCar'),
    path('approve/<int:car_id>/<int:profile_id>/', views.approve, name='approve'),
    path('negate/<int:car_id>/<int:profile_id>/', views.negate, name='negate'),
    path('managerConfirm/', views.managerConfirm, name='managerConfirm'),
    path('motorbikes/', views.motorbikes, name='motorbikes'),
    path('brands/', views.brands, name='brands'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('groups/', views.groups, name='groups'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('motorbike/<int:moto_id>/', views.motorbike_detail, name='motorbike_detail')
]
