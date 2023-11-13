from django import forms
from django.forms import ModelForm
from .models import Auto
from .models import Cliente
from .models import Producto


    # Agrega todos los campos necesarios para tu formulario

class AutoForm(forms.ModelForm):
    class Meta:
        model=Auto
        fields=["marca","modelo","anio"]

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=["nombre","apellido","contacto"]


class BusquedaForm(forms.Form):
        termino_busqueda = forms.CharField(max_length=100, required=False, label='Buscar')
        model=Producto
        fields=["categoria","precio"]
      

