from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Productos
from .models import Carrito, CarritoItem
from django.core.exceptions import ObjectDoesNotExist
from tienda.models import Moneda


# Create your views here.

def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregar_carrito(request, producto_id):
    producto = Productos.objects.get(id=producto_id)
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            carrito_id = _carrito_id(request)
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

def quitar_carrito(request, producto_id):
    carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    producto = get_object_or_404(Productos, id=producto_id)
    carrito_item = CarritoItem.objects.get(producto=producto, carrito=carrito)

    if carrito_item.cantidad > 1:
        carrito_item.cantidad -=1
        carrito_item.save()
    else:
        carrito_item.delete()
    return redirect('carrito')

def borrar_carrito(request, producto_id):
    carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    producto = get_object_or_404(Productos, id=producto_id)
    carrito_item = CarritoItem.objects.get(producto=producto, carrito=carrito)

    carrito_item.delete()
    return redirect('carrito')

def carrito(request, total=0, envio=0,totaltotal=0,cantidad=0, carrito_items=None):

    usd = Moneda.objects.get(titulo='Dolar')
    ars = Moneda.objects.get(titulo='Ars')
    

    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        carrito_items = CarritoItem.objects.filter(carrito=carrito, activo=True)
        for carrito_item in carrito_items:
            if ars.estado == True:
                if carrito_item.producto.oferta > 0:
                    total += (((carrito_item.producto.precio_ars * (100 - carrito_item.producto.oferta))/100) * carrito_item.cantidad)
                else:
                    total += (carrito_item.producto.precio_ars * carrito_item.cantidad)

            if usd.estado == True:
                if carrito_item.producto.oferta > 0:
                    total += (((carrito_item.producto.precio_usd * (100 - carrito_item.producto.oferta))/100) * carrito_item.cantidad)
                else:
                    total += (carrito_item.producto.precio_usd * carrito_item.cantidad)
             
            cantidad += carrito_item.cantidad
        envio = 1500
        totaltotal = total + envio
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'cantidad': cantidad,
        'carrito_items': carrito_items,
        'envio': envio,
        'totaltotal': totaltotal,
    }
    print(carrito_items)
    return render(request, 'carrito.html', context)