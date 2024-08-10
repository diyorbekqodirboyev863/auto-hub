from django.shortcuts import render, get_object_or_404
from .models import Car, Detail, Feature

# Home.
def home(request):
    '''View for the home page.'''
    cars = Car.objects.all()
    return render(request=request, template_name='home.html', context={'cars': cars})

# Car details.

def car_details(request, car_id):
    '''View for car details.'''
    car = get_object_or_404(Car, pk=car_id)
    detail = Detail.objects.get(car=car)
    feature = Feature.objects.get(car=car)
    return render(request=request, template_name='car_details.html', context={'car': car, 'detail': detail, 'feature': feature})