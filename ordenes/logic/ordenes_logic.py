from ..models import Orden

def get_ordenes():
    ordenes = Orden.objects.all()
    return list(ordenes.values('fecha_creacion', 'fecha_vencimiento', 'total', 'saldo_pendiente'))
