from .models import Categoria, Moneda

def menu_links(request):
    links = Categoria.objects.all()
    return dict(links=links)

def moneda(request):
    usd = Moneda.objects.get(titulo='Dolar')
    ars = Moneda.objects.get(titulo='Ars')

    if ars.estado == True:
        moneda = 'ARS'
    if usd.estado == True:
        moneda = 'USD'
    return dict(moneda=moneda)