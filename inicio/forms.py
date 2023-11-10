from django import forms
from django.forms import ModelForm
from .models import Auto

    # Agrega todos los campos necesarios para tu formulario

class AutoForm(forms.ModelForm):
    class Meta:
        model=Auto
        fields=["marca","modelo","anio"]

