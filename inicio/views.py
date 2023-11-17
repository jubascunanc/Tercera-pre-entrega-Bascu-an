
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutoForm
from .forms import ClienteForm
from .models import Auto
from .models import Cliente
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegistroForm
from .models import Producto



def formulario (request):

    if request.method=="POST":
        autocreado=AutoForm(request.POST)
        if autocreado.is_valid():
            autonuevo=autocreado.cleaned_data
            marca=autonuevo.get("marca")
            modelo=autonuevo.get("modelo")
            anio=autonuevo.get("anio")
            nuevoauto=Auto(marca=marca,modelo=modelo,anio=anio)
            nuevoauto.save()
            return redirect("index")
    else:
        return render(request, "form_templates.html",{
            "form": AutoForm
 
        })
    
def cliente (request):
    if request.method=="POST":
        clientecreado=ClienteForm(request.POST)
        if clientecreado.is_valid():
            clientenuevo=clientecreado.cleaned_data
            nombre=clientenuevo.get("nombre")
            apellido=clientenuevo.get("apellido")
            contacto=clientenuevo.get("contacto")
            nuevocliente=Cliente(nombre=nombre,apellido=apellido,contacto=contacto)
            nuevocliente.save()
            return redirect("index")
    else:
        return render(request, "contacto_templates.html",{
            "contacto": ClienteForm
        })
    
# views.py
class RegistroView(generic.CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'registro.html'


def about_me(request):
    # Puedes pasar información adicional si es necesario
    context = {
        'nombre': 'Juan José Bascuñán',
        'descripcion': 'Soy un entuasiasta de los autos deportivos.',
        'intereses': ['Automotriz', 'Mecanica Autos', 'Deportivo'],
        # Otros datos que desees mostrar en la página
    }
    return render(request, 'about_me.html', context)



def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})



def inicio(request):
    listaauto=Auto.objects.all().values()
    listacliente=Cliente.objects.all().values()
   
    return render(request, "mi_template.html",{
        "listaauto": listaauto,
        "listacliente":listacliente,
    
    })
