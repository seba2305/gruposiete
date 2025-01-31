from django.db import models

 

class TipoMedida(models.Model):
    id_tipo_medida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

class Verificacion(models.Model):
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

class Medida(models.Model):
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

class OrganismoSectorial(models.Model):
    id_os = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre}"
    
class Plan(models.Model):
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
