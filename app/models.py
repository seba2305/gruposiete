from django.db import models
from django.contrib.auth.models import User  # Importa el modelo User
from crum import get_current_user

class ModeloBase(models.Model):
    """
    Clase base abstracta que añade campos de auditoría para registros.
    
    Campos:
    - created_at: Fecha y hora de creación del registro
    - updated_at: Fecha y hora de la última actualización
    - created_by: Usuario que creó el registro
    - updated_by: Usuario que realizó la última modificación
    
    Utiliza la librería 'crum' para obtener el usuario actual de forma automática.
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    # Campo para el usuario que creó el registro
    created_by = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='%(class)s_created',
        null=True,
        blank=True
    )
    
    # Campo para el usuario que modificó el registro por última vez
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name='%(class)s_updated',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
            self.updated_by = user
        super(ModeloBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True  # Indica que esta clase es abstracta

class TipoMedida(ModeloBase):
    id_tipo_medida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

class Verificacion(ModeloBase):
    id_verificacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    verificacion = models.TextField(max_length=2000)
    
    def __str__(self):
        return f"{self.nombre} - {self.verificacion}"

FRECUENCIA = [
('ANUAL', 'Anual'),
('UNICA', 'Unica'),
('CADA_5_ANIOS', 'Cada 5 años'),
]

class Medida(ModeloBase):
    id_medida = models.AutoField(primary_key=True)
    referencia_pda = models.CharField(max_length=100)
    nombre_corto = models.CharField(max_length=100) 
    indicador = models.TextField(max_length=2000) 
    formula_de_calculo = models.TextField(max_length=2000) 
    frecuencia_reporte = models.CharField(max_length=30, choices=FRECUENCIA, default='ANUAL')
    tipo_de_dato_a_validar = models.CharField(max_length=100, blank=True, null=True) 
    id_tipo_medida = models.ForeignKey('TipoMedida', models.CASCADE, db_column='id_tipo_medida')
    id_plan = models.ForeignKey('Plan', models.CASCADE, db_column='id_plan')
    id_os = models.ForeignKey('OrganismoSectorial', models.CASCADE, db_column='id_os')
    verificaciones = models.ManyToManyField(Verificacion, through='VerificacionMedida')

    def __str__(self):
        return f"{self.nombre_corto} - {self.frecuencia_reporte}"
    
class VerificacionMedida(models.Model):
    id_verificacion = models.ForeignKey('Verificacion', models.CASCADE, db_column='id_verificacion')
    id_medida = models.ForeignKey('Medida', models.CASCADE, db_column='id_medida')

class OrganismoSectorial(ModeloBase):
    id_os = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Plan(ModeloBase):
    id_plan = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    inicio = models.DateTimeField(null=True)
    termino = models.DateTimeField(null=True)
    estado_avance = models.CharField(max_length=255, blank=True, null=True)
    organismos = models.ManyToManyField(OrganismoSectorial, through='OrganismoPlan')
   
    def __str__(self):
        return f"{self.id_plan} - {self.nombre}"
    
class OrganismoPlan(models.Model):
    id_os = models.ForeignKey('OrganismoSectorial', models.CASCADE, db_column='id_os')
    id_plan = models.ForeignKey('Plan', models.CASCADE, db_column='id_plan')


ESTADO_VERIFICACION = [
('VERIFICACION_PENDIENTE', 'Verificación pendiente'),
('VERIFICADA', 'Verificada'),
('RECHAZADA', 'Rechazada'),
]
class MedidaReportada(ModeloBase):
    id_medida_reportada = models.AutoField(primary_key=True)
    id_os = models.ForeignKey('OrganismoSectorial', models.CASCADE, db_column='id_os', help_text="Id del Organismo Sectorial que está informando.")
    id_medida = models.ForeignKey('Medida', models.CASCADE, db_column='id_medida', help_text="Id de la medida a resportar.")
    id_usuario = models.ForeignKey(User, models.CASCADE, help_text="Id Usuario de django.")
    valor = models.TextField(max_length=50, help_text="Resultado de la medida aplicada.")  
    estado = models.CharField(max_length=30, choices=ESTADO_VERIFICACION, default='VERIFICACION_PENDIENTE')
    