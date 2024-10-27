from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def cars(request):
    context = {}
    return render(request, 'cars.html', context)

def motorbikes(request):
    context = {}
    return render(request, 'motorbikes.html', context)

def brands(request):
    context = {}
    return render(request, 'brands.html', context)
