from django.urls import path
from . import views

 


from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from api.views import OrganismoSectorialViewSet, PlanViewSet, MedidaViewSet, VerificacionViewSet, TipoMedidaViewSet, MedidaReportadaViewSet
from django.urls import path, include



"""
DefaultRouter: Automatiza la generación de rutas para las vistas registradas. Evita escribir manualmente cada
endpoint.

register: Asocia el ViewSet con un prefijo de URL (productos). Esto crea rutas como:

include(router.urls): Incluye las rutas generadas por el router en las URLs de Django.

Por qué usar DefaultRouter:
Es la forma más eficiente de gestionar rutas para APIs CRUD. Si las rutas necesitan personalización, se pueden
combinar con otras en el mismo archivo.
"""



router = DefaultRouter() 
router.register(r'organismos', OrganismoSectorialViewSet)
router.register(r'planes', PlanViewSet)
router.register(r'medidas', MedidaViewSet)
router.register(r'verificaciones', VerificacionViewSet)
router.register(r'tipo_medidas', TipoMedidaViewSet)
router.register(r'medida_reportada', MedidaReportadaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]


