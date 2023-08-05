from django import forms
from .models import VehiculoModel

class VehiculoForm(forms.ModelForm):
    class meta:
        model = VehiculoModel
        fields = "__all__"