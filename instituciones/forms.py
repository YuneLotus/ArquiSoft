from django import forms
from .models import Grado, Estudiante

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = [
            'colegio',
            'codigo',
            'grado',
            'grupo',
            'descripcion',
            'jornada',
        ]

        labels = {
            'colegio' : 'Colegio',
            'codigo' : 'Codigo',
            'grado' : 'Grado',
            'grupo' : 'Grupo',
            'descripcion' : 'Descripcion',
            'jornada' : 'Jornada',
        }

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'codigo',
            'colegio',
            'nombre',
            'apellido',
            'grado',
            'acudientes',
        ]

        labels = {
            'codigo' : 'Codigo',
            'colegio' : 'Colegio',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'grado' : 'Grado',
            'acudientes' : 'Acudientes',
        }


