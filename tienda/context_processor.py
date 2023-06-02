from .models import Categoria, Moneda

def menu_links(request):
    links = Categoria.objects.all()
    return dict(links=links)

