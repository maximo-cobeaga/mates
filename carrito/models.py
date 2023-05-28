from django.db import models
from tienda.models import Productos

# Create your models here.
class Carrito(models.Model):
    carrito_id = models.CharField(max_length=100, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id

class CarritoItem(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    activo = models.BooleanField(default=True)

    def subtotal(self):
        return self.producto.precio_ars*self.cantidad

    def __unicode__(self):
        return self.producto