from django.contrib import admin
from .models import Categoria, Productos, Banners, Moneda
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

class ProductosAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Banners)
admin.site.register(Moneda)
