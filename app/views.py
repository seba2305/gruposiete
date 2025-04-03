from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import OrganismoSectorial, Plan, Medida, TipoMedida, Verificacion, MedidaReportada
from django.db import transaction

# Lista de cursos con paginación
def organismos(request):
    organismos = OrganismoSectorial.objects.all()
    paginator = Paginator(organismos, 10)  # 10 cursos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'organismos.html', {'page_obj': page_obj})

# Detalle de un curso
def detalle_organismo(request, id_os):
    medidas_reportadas = MedidaReportada.objects.filter(organismo_sectorial_id=id_os)

    print(f"ID del organismo recibido: {id_os}")
    print(f"Cantidad de medidas reportadas encontradas: {medidas_reportadas.count()}")
    for medida in medidas_reportadas:
        print(f"Medida ID: {medida.id}, Valor: {medida.valor}, Estado: {medida.estado}")

    return render(request, 'detalle_organismo.html', {
        'medidas_reportadas': medidas_reportadas,
    })

