from ..models import Cronograma

def get_cronogramas():
    cronogramas = Cronograma.objects.all()
    return list(cronogramas.values('concepto', 'descripcion', 'colegio', 'estudiantes'))

def create_cronograma(form):
    cronograma = form.save()
    cronograma.save()
    return ()

