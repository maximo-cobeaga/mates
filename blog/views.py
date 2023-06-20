from django.shortcuts import render
from tienda.models import Banners
from .models import PostModel


# Create your views here.
def blog(request):
    posts =  PostModel.objects.all()
    cont = 0
    for p in posts:
        cont += 1  

    return render(request,'blog.html', {
        'cont':cont,
        'posts':posts,
    })

def politica(request):
    return render(request, 'politica.html')

def regalos(request):
    return render(request,'regalos.html')