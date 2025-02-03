from django.shortcuts import render
from rest_framework import viewsets
from app.models import OrganismoSectorial, OrganismoPlan, Plan, VerificacionMedida, Medida, Verificacion, TipoMedida 
from .serializers import OrganismoSectorialSerializer, PlanSerializer, MedidaSerializer, VerificacionSerializer, TipoMedidaSerializer

# Create your views here.

"""
viewsets.ModelViewSet:
Una clase predefinida de DRF que simplifica la creación de vistas CRUD (Create, Read,
Update, Delete). Es más eficiente que escribir vistas separadas para cada acción.
Es ideal para operaciones CRUD estándar porque minimiza la cantidad de código, pero permite personalización si es
necesario

queryset = x.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
serializer_class = xSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.
"""



class OrganismoSectorialViewSet(viewsets.ModelViewSet):
    queryset = OrganismoSectorial.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
    serializer_class = OrganismoSectorialSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
    serializer_class = PlanSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.

class MedidaViewSet(viewsets.ModelViewSet):
    queryset = Medida.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
    serializer_class = MedidaSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.


class VerificacionViewSet(viewsets.ModelViewSet):
    queryset = Verificacion.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
    serializer_class = VerificacionSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.


class TipoMedidaViewSet(viewsets.ModelViewSet):
    queryset = TipoMedida.objects.all() # Define qué datos se manejarán en los endpoints. Se incluyen todos en este caso
    serializer_class = TipoMedidaSerializer #Conecta la vista con el serializer para que los datos se transformen correctamente a JSON y viceversa.




 