from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('politica', views.politica, name='politica'),
    path('regalos', views.regalos, name='regalos')
]