from ..models import Colegio

def get_colegios():
    queryset = Colegio.objects.all()
    return (queryset)

def create_colegio(form):
    colegio = form.save()
    colegio.save()
    return ()