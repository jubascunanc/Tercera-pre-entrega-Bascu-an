
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


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
