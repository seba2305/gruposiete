import pytest
from django.utils import timezone
from django.contrib.auth import get_user_model
from crum import set_current_user

from app.models import (
    OrganismoSectorial,
    Plan,
    TipoMedida,
    Medida,
    Verificacion,
    VerificacionMedida,
    MedidaReportada,
    OrganismoPlan
)

User = get_user_model()

# ---------- FIXTURE BASE PARA USUARIO Y ORGANISMO ----------

@pytest.fixture
def usuario_y_organismo(db):
    user = User.objects.create_user(username="fiscalizador_sag", password="1234")
    set_current_user(user)
    organismo = OrganismoSectorial.objects.create(nombre="SAG")
    user.organismo_sectorial = organismo
    user.save()
    return user, organismo

# ---------- TESTS ESTRUCTURADOS ----------

def test_crear_usuario_y_organismo(usuario_y_organismo):
    user, organismo = usuario_y_organismo
    assert user.organismo_sectorial == organismo
    assert str(organismo) == "SAG"

def test_crear_plan_y_relacionarlo_a_organismo(usuario_y_organismo):
    user, organismo = usuario_y_organismo

    plan = Plan.objects.create(
        nombre="Plan Nacional de Fiscalización Sanitaria",
        inicio=timezone.now(),
        termino=timezone.now() + timezone.timedelta(days=365),
        estado_avance="En ejecución"
    )
    OrganismoPlan.objects.create(plan=plan, organismo_sectorial=organismo)

    assert plan.organismos.count() == 1
    assert plan.created_by == user
    assert str(plan) == "Plan Nacional de Fiscalización Sanitaria"

def test_crear_tipo_de_medida(usuario_y_organismo):
    user, _ = usuario_y_organismo

    tipo = TipoMedida.objects.create(nombre="Controles sanitarios")
    assert str(tipo) == "Controles sanitarios"
    assert tipo.created_by == user

def test_crear_medida_completa(usuario_y_organismo):
    user, organismo = usuario_y_organismo

    plan = Plan.objects.create(
        nombre="Plan de Medición SAG",
        inicio=timezone.now(),
        termino=timezone.now() + timezone.timedelta(days=90),
        estado_avance="Planificado"
    )
    OrganismoPlan.objects.create(plan=plan, organismo_sectorial=organismo)

    tipo = TipoMedida.objects.create(nombre="Cantidad de fiscalizaciones")

    medida = Medida.objects.create(
        referencia_pda="SAG-2025",
        nombre_corto="Fiscalización predial",
        indicador="N° de predios fiscalizados",
        formula_de_calculo="sum(fiscalizaciones)",
        frecuencia_reporte="ANUAL",
        tipo_de_dato_a_validar="Entero",
        tipo_medida=tipo,
        plan=plan,
        organismo_sectorial=organismo
    )

    assert medida.created_by == user
    assert str(medida) == "Fiscalización predial - ANUAL"

def test_verificaciones_asociadas_a_medida(usuario_y_organismo):
    user, organismo = usuario_y_organismo

    plan = Plan.objects.create(nombre="Plan Verificación", inicio=timezone.now(), termino=timezone.now())
    tipo = TipoMedida.objects.create(nombre="Tipo Verificación")

    medida = Medida.objects.create(
        referencia_pda="VER-001",
        nombre_corto="Chequeo",
        indicador="Indicador de chequeo",
        formula_de_calculo="check()",
        frecuencia_reporte="UNICA",
        tipo_de_dato_a_validar="Boolean",
        tipo_medida=tipo,
        plan=plan,
        organismo_sectorial=organismo
    )

    ver1 = Verificacion.objects.create(nombre="Documento firmado", verificacion="Firmado por técnico")
    ver2 = Verificacion.objects.create(nombre="Informe digital", verificacion="Emitido desde plataforma")

    VerificacionMedida.objects.create(medida=medida, verificacion=ver1)
    VerificacionMedida.objects.create(medida=medida, verificacion=ver2)

    assert medida.verificaciones.count() == 2
    assert ver1.created_by == user

def test_reportar_medida(usuario_y_organismo):
    user, organismo = usuario_y_organismo

    plan = Plan.objects.create(nombre="Plan Reporte", inicio=timezone.now(), termino=timezone.now())
    tipo = TipoMedida.objects.create(nombre="Cantidad")

    medida = Medida.objects.create(
        referencia_pda="REP-001",
        nombre_corto="Reporte",
        indicador="N° total",
        formula_de_calculo="total()",
        frecuencia_reporte="ANUAL",
        tipo_de_dato_a_validar="Entero",
        tipo_medida=tipo,
        plan=plan,
        organismo_sectorial=organismo
    )

    medida_reportada = MedidaReportada.objects.create(
        organismo_sectorial=organismo,
        medida=medida,
        valor="101",
        estado="VERIFICACION_PENDIENTE"
    )

    assert medida_reportada.created_by == user
    assert medida_reportada.estado == "VERIFICACION_PENDIENTE"
    assert medida_reportada.medida == medida
