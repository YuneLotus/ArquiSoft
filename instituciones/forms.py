from django import forms
from .models import Colegio

class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegio
        fields = [
            'nit',
            'nombre',
            'direccion',
            'telefono',
        ]
        labels = {
            'nit': 'Nit',
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
        }

