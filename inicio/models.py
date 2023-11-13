
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Auto(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio= models.IntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)


class PerfilUsuario(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)


