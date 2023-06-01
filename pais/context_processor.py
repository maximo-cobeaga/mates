from django.http import HttpResponse
from .form import PaisForm

def seleccionar_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            pais_seleccionado = form.cleaned_data['pais']
            form.save()
            return HttpResponse('<h2>Formulario enviado</h2>')
    else:
        form = PaisForm()
        return dict(form=form)