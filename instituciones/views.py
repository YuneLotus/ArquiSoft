from django.shortcuts import render
from django.http import JsonResponse
from .forms import ColegioForm
from .logic.colegios_logic import get_colegios, create_colegio

# Create your views here.

def colegios_list(request):
    colegios = get_colegios()  # Obtiene la lista de colegios
    response_data = {
        'variable_list': colegios
    }
    return JsonResponse(response_data)
