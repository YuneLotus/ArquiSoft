from django import forms
from .models import Cronograma

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = Cronograma
        fields = [
            'concepto',
            'descripcion',
            'colegio',
            'estudiantes',
        ]

        labels = {
            'concepto' : 'Concepto',
            'descripcion' : 'Descripcion',
            'colegio' : 'Colegio',
            'estudiantes' : 'Estudiantes',
        }