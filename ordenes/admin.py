from django.contrib import admin

# Register your models here.
from .models import Orden, Factura, MetodoPago, Descuento

admin.site.register(Orden)
admin.site.register(Factura)
admin.site.register(MetodoPago)
admin.site.register(Descuento)