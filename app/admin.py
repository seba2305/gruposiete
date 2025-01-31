from django.contrib import admin

# Register your models here.
from .models import TipoMedida, Medida, VerificacionMedida, Verificacion, Plan, OrganismoPlan, OrganismoSectorial

@admin.register(OrganismoSectorial)
class OrganismoSectorialAdmin(admin.ModelAdmin):
    list_display = ('id_os', 'nombre')
    search_fields = ('nombre',)

@admin.register(TipoMedida)
class TipoMedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Verificacion)
class VerificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'verificacion')
    search_fields = ('verificacion', 'nombre') 

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id_medida', 'id_plan', 'id_tipo_medida', 'id_os', 'referencia_pda', 'nombre_corto')
    search_fields = ('referencia_pda', 'id_os','nombre_corto')
    list_filter = ('id_os',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id_plan', 'nombre', 'inicio', 'termino')
    search_fields = ('nombre','inicio') 

@admin.register(OrganismoPlan)
class OrganismoPlanAdmin(admin.ModelAdmin):
    list_display = ('id_plan', 'id_os')
    search_fields = ('id_plan', 'id_os')

@admin.register(VerificacionMedida)
class VerificacionMedidaAdmin(admin.ModelAdmin):
    list_display = ('id_medida', 'id_verificacion')
    search_fields = ('id_medida', 'id_verificacion')

