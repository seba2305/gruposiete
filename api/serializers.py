from rest_framework import serializers
from app.models import OrganismoSectorial, OrganismoPlan, Plan, VerificacionMedida, Medida, Verificacion, TipoMedida 


class OrganismoSectorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganismoSectorial
        fields = '__all__' #cada campo que queremos vaya en el serialozador 

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__' #cada campo que queremos vaya en el serialozador 

class MedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medida
        fields = '__all__' #cada campo que queremos vaya en el serialozador 

class VerificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verificacion
        fields = '__all__' #cada campo que queremos vaya en el serialozador 

class TipoMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMedida
        fields = '__all__' #cada campo que queremos vaya en el serialozador 




