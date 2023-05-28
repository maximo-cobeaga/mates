from django.shortcuts import render, get_object_or_404
from .models import Productos, Banners, Categoria
from carrito.models import  CarritoItem
from carrito.views import _carrito_id


# Create your views here.
def tienda(request, categoria_slug=None):

    categorias = None
    producto = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Productos.objects.filter(categoria=categorias, active=True)
        return render(request,'tienda.html', {
            'productos':productos
        })
    else:
        try:
            banners = Banners.objects.all()
            productos = Productos.objects.filter(active=True)
            return render(request,'tienda.html',{
                'productos': productos,
                'banners': banners
            })
        except:
            productos = Productos.objects.filter(active=True)
            return render(request,'tienda.html',{
                'banners':banners
            })
        

def detalle_producto(request,categoria_slug ,producto_slug):
    try:
        producto = Productos.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
        en_carrito = CarritoItem.objects.filter(carrito__carrito_id=_carrito_id(request), producto=producto).exists()

    except Exception as e:
        raise e
    if producto.oferta != 0:
        precio_oferta = (producto.precio_ars * (100 - producto.oferta))/100
        context = {
        'producto': producto,
        'en_carrito':en_carrito,
        'ofert':True,
        'precio_oferta':precio_oferta,
        }
    else:
        context = {
            'producto': producto,
            'en_carrito':en_carrito,
            'ofert': False
        }
    return render(request, 'detalle_producto.html', context)