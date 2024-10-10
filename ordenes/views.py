from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from .forms import MetodoPagoForm
from .logic.metodos_pago_logic import get_metodos_pago, create_metodo_pago

# Create your views here.

def metodos_pago_list(request):
    metodosPago = get_metodos_pago()  # Obtiene la lista de colegios
    response_data = {
        'metodos_pago_list': metodosPago
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
