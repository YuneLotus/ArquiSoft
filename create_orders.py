import os
import django
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ofipensiones.settings')
django.setup()

from ordenes.models import Orden

# Función para crear órdenes
def create_orders(num_orders):
    for _ in range(num_orders):
        fecha_vencimiento = timezone.make_aware(datetime(2024, 12, random.randint(3, 7)))
        total = 400000
        saldo_pendiente = random.uniform(0, 400000)
        
        Orden.objects.create(
            fecha_vencimiento=fecha_vencimiento,
            total=total,
            saldo_pendiente=saldo_pendiente
        )

if __name__ == "__main__":
    create_orders(10000)
    print("10,000 órdenes creadas exitosamente.")