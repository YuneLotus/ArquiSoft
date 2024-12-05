from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from .forms import MetodoPagoForm
from .logic.metodos_pago_logic import get_metodos_pago, create_metodo_pago
from .logic.ordenes_logic import get_ordenes
from .models import Orden
from django.utils.dateparse import parse_datetime
from django.utils import timezone

# Create your views here.

def metodos_pago_list(request):
    metodosPago = get_metodos_pago()  # Obtiene la lista de colegios
    response_data = {
        'metodos_pago_list': metodosPago
    }
    return JsonResponse(response_data)

def ordenes_list(request):
    ordenes = get_ordenes()  # Obtiene la lista de ordenes
    response_data = {
        'ordenes_list': ordenes
    }
    return JsonResponse(response_data)

def metodo_pago_create(request):
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            create_metodo_pago(form)
            return JsonResponse({'message': 'Successfully created metodo pago'}, status=201)
        else:
            print(form.errors)
            return JsonResponse({'errors': form.errors}, status=400)  # Retornar errores del formulario
    else:
        return JsonResponse({'error': 'No action taken, please submit a POST request.'}, status=400)

def filtrar_ordenes(request):
    # Obtener los parámetros de filtro de la solicitud GET
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    saldo_minimo = request.GET.get('saldo_minimo')
    saldo_maximo = request.GET.get('saldo_maximo')

    # Construir la consulta con los filtros
    ordenes = Orden.objects.all()

    if fecha_inicio:
        fecha_inicio = parse_datetime(fecha_inicio)
        if fecha_inicio:
            fecha_inicio = timezone.make_aware(fecha_inicio)
            ordenes = ordenes.filter(fecha_creacion__gte=fecha_inicio)
    if fecha_fin:
        fecha_fin = parse_datetime(fecha_fin)
        if fecha_fin:
            fecha_fin = timezone.make_aware(fecha_fin)
            ordenes = ordenes.filter(fecha_creacion__lte=fecha_fin)
    if saldo_minimo:
        ordenes = ordenes.filter(saldo_pendiente__gte=saldo_minimo)
    if saldo_maximo:
        ordenes = ordenes.filter(saldo_pendiente__lte=saldo_maximo)

    # Convertir los resultados a un formato JSON
    ordenes_data = list(ordenes.values())

    return JsonResponse(ordenes_data, safe=False)