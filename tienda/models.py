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
    precio_usd = models.IntegerField()
    oferta = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='fotos/productos')
    slug = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    active = models.BooleanField()

    def get_url(self):
        return reverse('detalle_producto', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.titulo

class Banners(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/banners')

    def __str__(self):
        return self.titulo