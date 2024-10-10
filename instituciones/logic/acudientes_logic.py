from ..models import Acudiente

def get_acudientes():
    acudientes = Acudiente.objects.all()
    return list(acudientes.values('cedula', 'nombre', 'apellido', 'telefono'))