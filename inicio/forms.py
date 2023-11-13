from django import forms
from django.forms import ModelForm
from .models import Auto
from .models import Cliente
from .models import User
from django.contrib.auth.forms import UserCreationForm



    # Agrega todos los campos necesarios para tu formulario

class AutoForm(forms.ModelForm):
    class Meta:
        model=Auto
        fields=["marca","modelo","anio"]

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=["nombre","apellido","contacto"]

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
