from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.titulo

class Productos(models.Model):
    titulo = models.CharField(max_length=100)
    precio_ars = models.IntegerField()
    precio_usd = models.IntegerField()
    oferta = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='fotos/productos')
    slug = models.CharField(max_length=100, unique=True)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    active = models.BooleanField()

    def __str__(self):
        return self.titulo