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
    
    def en_oferta(self):
        if self.producto.oferta != 0:
            precio_total = (self.producto.precio_ars * (100 - self.producto.oferta)) /100
            return round(precio_total)
        
    def en_oferta_usd(self):
        if self.producto.oferta != 0:
            precio_total = (self.producto.precio_usd * (100 - self.producto.oferta)) /100
            return round(precio_total)
    
    def subtotal(self):
        if self.producto.oferta != 0:
            return round(self.en_oferta()*self.cantidad)
        else:
            return round(self.producto.precio_ars*self.cantidad)
        
    def subtotal_usd(self):
        if self.producto.oferta != 0:
            return round(self.en_oferta_usd()*self.cantidad)
        else:
            return round(self.producto.precio_usd*self.cantidad)
    
    def __unicode__(self):
        return self.producto