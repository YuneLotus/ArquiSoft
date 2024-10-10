from ..models import Estudiante

def get_estudiantes():
    estudiantes = Estudiante.objects.all()
    return list(estudiantes.values('codigo', 'colegio', 'nombre', 'apellido', 'grado', 'acudientes'))

def create_estudiante(form):
    estudiante = form.save()
    estudiante.save()
    return ()