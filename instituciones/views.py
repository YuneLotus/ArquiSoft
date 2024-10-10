from django.shortcuts import render
from django.http import JsonResponse
from .forms import GradoForm, EstudianteForm
from .logic.colegios_logic import get_colegios
from .logic.grados_logic import get_grados, create_grado
from .logic.acudientes_logic import get_acudientes
from .logic.estudiantes_logic import get_estudiantes, create_estudiante

# Create your views here.

def colegios_list(request):
    colegios = get_colegios()  # Obtiene la lista de colegios
    response_data = {
        'colegios_list': colegios
    }
    return JsonResponse(response_data)

def grados_list(request):
    grados = get_grados()  # Obtiene la lista de colegios
    response_data = {
        'grados_list': grados
    }
    return JsonResponse(response_data)

def grado_create(request):
    if request.method == 'POST':
        form = GradoForm(request.POST)
        if form.is_valid():
            create_grado(form)
            return JsonResponse({'message': 'Successfully created grado'}, status=201)
        else:
            print(form.errors)
            return JsonResponse({'errors': form.errors}, status=400)  # Retornar errores del formulario
    else:
        return JsonResponse({'error': 'No action taken, please submit a POST request.'}, status=400)

def estudiantes_list(request):
    estudiantes = get_estudiantes()  # Obtiene la lista de colegios
    response_data = {
        'grados_list': estudiantes
    }
    return JsonResponse(response_data)

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            create_estudiante(form)
            return JsonResponse({'message': 'Successfully created estudiante'}, status=201)
        else:
            print(form.errors)
            return JsonResponse({'errors': form.errors}, status=400)  # Retornar errores del formulario
    else:
        return JsonResponse({'error': 'No action taken, please submit a POST request.'}, status=400)

def acudientes_list(request):
    acudientes = get_acudientes()  # Obtiene la lista de colegios
    response_data = {
        'acudientes_list': acudientes
    }
    return JsonResponse(response_data)
