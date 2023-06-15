from .models import Carrito, CarritoItem
from .views import _carrito_id

def contador(request):
    carrito_contador = 0

    try:
        carrito = Carrito.objects.filter(carrito_id=_carrito_id(request))
        carrito_items = CarritoItem.objects.all().filter(carrito=carrito[:1])

        for carrito_item in carrito_items:
            carrito_contador += carrito_item.cantidad
    except Carrito.DoesNotExist:
        carrito_contador=0
    return dict(carrito_contador=carrito_contador)


