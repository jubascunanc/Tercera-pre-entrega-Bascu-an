
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AutoForm
from .models import Auto

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

def inicio(request):
    listaauto=Auto.objects.all().values()
    return render(request, "mi_template.html",{
        "listaauto": listaauto,
    })