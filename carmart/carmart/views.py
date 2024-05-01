from django.shortcuts import render
from cars.models import CarsModel
from brands.models import BrandsModel

def base(request):
    return render(request, 'base.html')

def home(request, brands_slug=None):
    cars = CarsModel.objects.all()
    if brands_slug is not None:
        brands = BrandsModel.objects.get(slug = brands_slug)
        cars = CarsModel.objects.filter(brands = brands)
    brands = BrandsModel.objects.all()
    return render(request, 'home.html', {'cars' : cars, 'brands' : brands})




