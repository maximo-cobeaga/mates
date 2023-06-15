from django.shortcuts import render, get_object_or_404, redirect
from .models import Productos, Banners, Categoria, Moneda
from carrito.models import  CarritoItem
from carrito.views import _carrito_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

# Create your views here.


def tienda(request, categoria_slug=None):

    # usd = Moneda.objects.get(titulo='Dolar')
    # ars = Moneda.objects.get(titulo='Ars')

    # if usd.estado == True:
    #     moneda = 'USD'
    # if ars.estado == True:
    #     moneda = 'ARS'

    # print(usd.estado)
    # print(ars.estado)

    categorias = None
    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Productos.objects.filter(categoria=categorias, active=True)
        counter = 0
        for p in productos:
            counter += 1
        return render(request,'tienda.html', {
            'productos':productos,
            'counter': counter,
            # 'moneda': moneda,
        })
    else:
        try:
            banners = Banners.objects.all()
            productos = Productos.objects.filter(active=True)
            paginator = Paginator(productos, 12)
            page = request.GET.get('page')
            page_producto = paginator.get_page(page)

            return render(request,'tienda.html',{
                'productos': page_producto,
                'banners': banners,
                # 'moneda': moneda,
            })
        except:
            productos = Productos.objects.filter(active=True)
            return render(request,'tienda.html',{
                'banners':banners,
            })
        

def detalle_producto(request,categoria_slug ,producto_slug):

    # usd = Moneda.objects.get(titulo='Dolar')
    # ars = Moneda.objects.get(titulo='Ars')

    # if usd.estado == True:
    #     moneda = 'USD'
    # if ars.estado == True:
    #     moneda = 'ARS'

    try:
        producto = Productos.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
        en_carrito = CarritoItem.objects.filter(carrito__carrito_id=_carrito_id(request), producto=producto).exists()
    except Exception as e:
        raise e
    
    context = {
    'producto': producto,
    'en_carrito':en_carrito,
    # 'moneda': moneda
    }
    return render(request, 'detalle_producto.html', context)


def cambiar_estado(request, moneda):
    if request.method == 'POST':
        mon = Moneda.objects.get(titulo=moneda)
        mons = Moneda.objects.all()
        for m in mons:
            if m.estado == True:
                m.estado = False
                m.save()
        mon.estado = True
        mon.save()
        print(mon.titulo,' - ',mon.estado)

    return redirect('tienda')
