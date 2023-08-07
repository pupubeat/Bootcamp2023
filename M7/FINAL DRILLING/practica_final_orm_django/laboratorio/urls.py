from django.urls import path
from .views import registro_view, login_view, logout_view, \
    homeView, listadoView, agregarView, eliminarView, editarView

urlpatterns = [
    path('listado/editarlaboratorio/<id>', editarView, name='editar'),
    path('listado/eliminarlaboratorio/<id>', eliminarView, name='eliminar'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', homeView, name ='home'),
    path('listado/', listadoView, name ='listado'),
    path('agregar/', agregarView, name ='agregar'),
]