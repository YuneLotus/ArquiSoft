from ..models import Colegio

def get_colegios():
    colegios = Colegio.objects.all()
    return list(colegios.values('nit', 'nombre', 'direccion', 'telefono'))

def create_colegio(form):
    colegio = form.save()
    colegio.save()
    return ()


