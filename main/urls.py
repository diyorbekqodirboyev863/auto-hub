from django.urls import path
from . import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='car_details/<int:car_id>', view=views.car_details, name='car_details'),
] 