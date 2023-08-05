from django.shortcuts import render
from django.contrib import messages
from .forms import VehiculoForm

def IndexView(request):
    return render (request, 'index.html', {})

def AddVehiculo(request):
    form = VehiculoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = VehiculoForm()
        messages.success(request, 'Los datos se han procesado exitosamente')

    return render(request, "addform.html", {'form':form})

