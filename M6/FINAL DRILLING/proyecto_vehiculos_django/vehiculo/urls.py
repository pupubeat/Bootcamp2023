from django.urls import path
from .views import IndexView, AddVehiculo

urlpatterns = [
    path('', IndexView, name = 'index'),
    path('vehiculo/add/', AddVehiculo, name = 'addvehiculo')
]