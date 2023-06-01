from django import forms
from django_countries.fields import CountryField

class PaisForm(forms.Form):
    pais = CountryField().formfield()