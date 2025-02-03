from rest_framework import serializers
from app.models import OrganismoSectorial 


class OrganismoSectorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganismoSectorial
        fields = '__all__' #cada campo que queremos vaya en el serialozador 




