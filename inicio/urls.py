from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='index'),
    path('formulario',views.formulario, name='form'),
    path('cliente',views.cliente, name='contacto.urls')
]

 