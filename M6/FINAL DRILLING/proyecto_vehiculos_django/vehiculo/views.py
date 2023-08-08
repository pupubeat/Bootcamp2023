from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VehiculoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm
from django.http import HttpResponseRedirect

def indexView(request):
    return render (request, 'index.html', {})

def AddVehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos se han procesado exitosamente.') 
            return redirect('/#')
    else:
        form = VehiculoForm()

    return render(request, "addform.html", {'form':form})

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
