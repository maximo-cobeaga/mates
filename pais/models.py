from django.db import models

# Create your models here.
class Pais(models.Model):
    titulo = models.CharField(max_length=10)

    def __str__(self):
        return self.titulo