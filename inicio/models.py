
# Create your models here.
from django.db import models

# Create your models here.
class Auto(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio= models.IntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)

class Producto(models.Model):
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()