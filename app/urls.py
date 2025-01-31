from django.urls import path
from . import views

urlpatterns = [
    path('', views.organismos, name='organismos'),
    path('<str:id_os>/', views.detalle_organismo, name='detalle_organismo'),

]
