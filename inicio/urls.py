from django.urls import path
from . import views
from django.urls import path
from .views import RegistroView
from .views import about_me
from .views import listar_productos



urlpatterns = [
    path('',views.inicio, name='index'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('about_me/', about_me, name='about_me'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('formulario',views.formulario, name='form'),
    path('cliente',views.cliente, name='contacto.urls')
]

