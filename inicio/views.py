
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutoForm
from .forms import ClienteForm
from .models import Auto
from .models import Cliente
from .models import Producto
from .forms import BusquedaForm



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
    

def busqueda(request):
    if request.method == 'GET':
        form = BusquedaForm(request.GET)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Producto.objects.filter(nombre__icontains=termino_busqueda)
        else:
            resultados = Producto.objects.all()
    else:
        form = BusquedaForm()
        resultados = Producto.objects.all().values()

    return render(request, 'buscar_productos.html', {
        'resultados': BusquedaForm
        })


def inicio(request):
    listaauto=Auto.objects.all().values()
    listacliente=Cliente.objects.all().values()
    listabusqueda=Producto.objects.all().values()
    return render(request, "mi_template.html",{
        "listaauto": listaauto,
        "listacliente":listacliente,
        "listabusqueda":listabusqueda,
    })