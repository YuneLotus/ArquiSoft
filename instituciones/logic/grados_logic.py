from ..models import Grado

def get_grados():
    grados = Grado.objects.all()
    return list(grados.values('colegio', 'codigo', 'grado', 'grupo', 'descripcion', 'jornada'))

def create_grado(form):
    grado = form.save()
    grado.save()
    return ()
