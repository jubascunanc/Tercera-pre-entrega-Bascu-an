
# Create your views here.
from django.shortcuts import render


def inicio(request):

    return render(request,"mi_template.html")
    
 