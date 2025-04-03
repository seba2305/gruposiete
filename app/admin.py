from django.contrib import admin

# Register your models here.
from .models import TipoMedida, Medida, VerificacionMedida, Verificacion, Plan, OrganismoPlan, OrganismoSectorial, MedidaReportada, CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(OrganismoSectorial)
class OrganismoSectorialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(TipoMedida)
class TipoMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    search_fields = ('nombre',)

@admin.register(Verificacion)
class VerificacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'verificacion')
    search_fields = ('verificacion', 'nombre') 

@admin.register(Medida)
class MedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'plan', 'tipo_medida', 'organismo_sectorial', 'referencia_pda', 'nombre_corto')
    search_fields = ('referencia_pda', 'organismo_sectorial','nombre_corto')
    list_filter = ('organismo_sectorial',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'inicio', 'termino')
    search_fields = ('nombre','inicio') 

@admin.register(OrganismoPlan)
class OrganismoPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'organismo_sectorial','plan')
    search_fields = ('plan', 'organismo_sectorial')

@admin.register(VerificacionMedida)
class VerificacionMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'medida', 'verificacion')
    search_fields = ('medida', 'verificacion')

@admin.register(MedidaReportada)
class MedidaReportadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'medida', 'valor','organismo_sectorial','estado')
    search_fields = ('medida', 'organismo_sectorial')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'organismo_sectorial']

    fieldsets = UserAdmin.fieldsets + (
        ('Campos personalizados', {
            'fields': ('organismo_sectorial',),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Campos personalizados', {
            'fields': ('organismo_sectorial',),
        }),
    )