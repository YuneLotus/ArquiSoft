from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from .forms import CronogramaForm
from .logic.cronogramas_logic import get_cronogramas, create_cronograma

# Create your views here.

def cronogramas_list(request):
    cronogramas = get_cronogramas()  # Obtiene la lista de colegios
    response_data = {
        'cronogramas_list': cronogramas
    }
    return JsonResponse(response_data)

def cronograma_create(request):
    if request.method == 'POST':
        form = CronogramaForm(request.POST)
        if form.is_valid():
            create_cronograma(form)
            return JsonResponse({'message': 'Successfully created cronograma'}, status=201)
        else:
            print(form.errors)
            return JsonResponse({'errors': form.errors}, status=400)  # Retornar errores del formulario
    else:
        return JsonResponse({'error': 'No action taken, please submit a POST request.'}, status=400)
