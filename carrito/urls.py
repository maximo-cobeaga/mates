from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('quitar_carrito/<int:producto_id>/', views.quitar_carrito, name='quitar_carrito'),
    path('borrar_carrito/<int:producto_id>/', views.borrar_carrito, name='borrar_carrito'),
]