from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def get_url(self):
        return reverse('produtos_categoria', args=[self.slug])

    def __str__(self):
        return self.titulo
    

class Productos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200, null=True)
    precio_ars = models.IntegerField()
    precio_usd = models.IntegerField(null=True)
    oferta = models.IntegerField(default=0, null=True)
    imagen = models.ImageField(upload_to='fotos/productos')
    slug = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    active = models.BooleanField()
    precio_final = models.IntegerField(null=True,blank=True)

    def get_url(self):
        return reverse('detalle_producto', args=[self.categoria.slug, self.slug])
    
    def in_oferta_ars(self):
        if self.oferta > 0:
            precio = round((self.precio_ars * (100 - self.oferta))/ 100)
            return dict(precio=precio)
        
    def in_oferta_usd(self):
        if self.oferta > 0:
            precio = round((self.precio_usd * (100 - self.oferta))/ 100)
            return dict(precio=precio)
        

    def __str__(self):
        return self.titulo

class Banners(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/banners')

    def __str__(self):
        return self.titulo
    
class Moneda(models.Model):
    titulo = models.CharField(max_length=5)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo