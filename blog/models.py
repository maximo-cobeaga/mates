from django.db import models

# Create your models here.
class PostModel(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=50,blank=True,null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo