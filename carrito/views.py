from django.shortcuts import render, redirect
from tienda.models import Productos
from .models import Carrito, CarritoItem

# Create your views here.

def _carrito_id(request):
    carrito = request.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, producto_id):
    producto = Productos.objects.get(id=producto_id)
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = carrito.objects.create(
            carrito_id = _carrito_id
        )
    carrito.save()

    try:
        carrito_item = CarritoItem.objects.get(producto=producto, carrito=carrito)
        carrito_item.cantidad += 1
        carrito_item.save()
    except CarritoItem.DoesNotExist:
        carrito_item =CarritoItem.objects.create(
            producto= producto,
            cantidad = 1,
            carrito = carrito,
        )
        carrito_item.save()
    return redirect('carrito')


def carrito(request):
    return render(request, 'carrito.html')