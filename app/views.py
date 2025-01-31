from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import OrganismoSectorial, Plan, Medida, TipoMedida, Verificacion
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
    organismo= get_object_or_404(OrganismoSectorial, id_os=id_os)

    return render(request, 'detalle_organismo.html', {
        'organismo': organismo,
    })

