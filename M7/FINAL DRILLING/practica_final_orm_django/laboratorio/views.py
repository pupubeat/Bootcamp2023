from django.shortcuts import render, redirect
from .models import Laboratorio, DirectorGeneral, Producto
from .forms import LaboratorioForm, DirectorGeneralForm, ProductoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django import forms
from .models import BoardsModel
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import InputForm, BoardsForm, RegistroUsuarioForm
from django.shortcuts import get_object_or_404, redirect


def homeView(request):
    context = {}
    return render(request, 'home.html', context)

def listadoView(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'listado.html', {'laboratorios': laboratorios})

def eliminarView(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id) 
    laboratorio.delete()
    messages.success(request, 'Laboratorio eliminado con éxito') 
    return redirect('/listado')

def editarView(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio editado con éxito.')
            return redirect('/listado') 
    else:
        form = LaboratorioForm(instance=laboratorio)

    return render(request, 'editar.html', {'form': form})

def agregarView(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Laboratorio agregado con éxito.') 
            return redirect('home')
    else:
        form = LaboratorioForm()
    
    return render(request, 'agregar.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como : {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"Username o Password inválidos.")
        else:
            messages.error(request,"Username o Password inválidos.")

    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario registrado con éxito.")
            return HttpResponseRedirect('/')
    
        messages.error(request, "Registro invalido. Algunos de los datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)

