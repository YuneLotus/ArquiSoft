from ..models import MetodoPago

def get_metodos_pago():
    metodosPago = MetodoPago.objects.all()
    return list(metodosPago.values('colegio', 'nombre', 'descripcion'))

def create_metodo_pago(form):
    metodoPago = form.save()
    metodoPago.save()
    return ()
