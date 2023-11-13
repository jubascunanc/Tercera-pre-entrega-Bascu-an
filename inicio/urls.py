from django.urls import path
from . import views
# urls.py
from django.urls import path
from .views import RegistroView


urlpatterns = [
    path('',views.inicio, name='index'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('formulario',views.formulario, name='form'),
    path('cliente',views.cliente, name='contacto.urls')
]


