from django.shortcuts import render
from django.http import JsonResponse
from .models import Orden

# Create your views here.

def filtrar_ordenes(request):
    # Obtener los parámetros de filtro de la solicitud GET
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    estado = request.GET.get('estado')
    monto_minimo = request.GET.get('monto_minimo')
    monto_maximo = request.GET.get('monto_maximo')

    # Construir la consulta con los filtros
    ordenes = Orden.objects.all()

    if fecha_inicio:
        ordenes = ordenes.filter(fecha__gte=fecha_inicio)
    if fecha_fin:
        ordenes = ordenes.filter(fecha__lte=fecha_fin)
    if estado:
        ordenes = ordenes.filter(estado=estado)
    if monto_minimo:
        ordenes = ordenes.filter(monto__gte=monto_minimo)
    if monto_maximo:
        ordenes = ordenes.filter(monto__lte=monto_maximo)

    # Convertir los resultados a un formato JSON
    ordenes_data = list(ordenes.values())

    return JsonResponse(ordenes_data, safe=False)

