from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_notificaciones, name='listar-notificaciones'),
    path('no-leidas/', views.notificaciones_no_leidas, name='notificaciones-no-leidas'),
    path('<int:pk>/marcar-leida/', views.marcar_notificacion_leida, name='marcar-notificacion-leida'),
] 