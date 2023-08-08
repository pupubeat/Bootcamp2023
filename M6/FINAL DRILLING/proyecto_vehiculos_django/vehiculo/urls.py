from django.urls import path
from .views import indexView, AddVehiculo, registro_view, login_view, logout_view

urlpatterns = [
    path('', indexView, name = 'index'),
    path('vehiculo/add/', AddVehiculo, name = 'addvehiculo'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]