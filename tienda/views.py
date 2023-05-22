from django.shortcuts import render
from .models import Productos


# Create your views here.
def tienda(request):
    try:
        productos = Productos.objects.all()
        return render(request,'tienda.html',{
            'productos': productos 
        })
    except:
        return render(request,'tienda.html')