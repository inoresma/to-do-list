from django.utils import timezone
from datetime import timedelta
from django.db.models import Q
from apps.notificaciones_app.models import Notificacion

def verificar_tareas_por_vencer(usuario):
    from .models import Tarea
    
    tiempo_actual = timezone.now()
    tiempo_limite = tiempo_actual + timedelta(days=1)
    
    # Verificar tareas próximas a vencer (solo las que no tienen notificación activa)
    tareas_proximas = Tarea.objects.filter(
        usuario=usuario,
        fecha_vencimiento__range=(tiempo_actual, tiempo_limite),
        estado__in=['pendiente', 'en_progreso']
    ).exclude(
        id__in=Notificacion.objects.filter(
            usuario=usuario,
            tipo='fecha_vencimiento',
            leida=False
        ).values_list('tarea_id', flat=True)
    )
    
    # Verificar tareas vencidas no completadas (solo las que no tienen notificación activa)
    tareas_vencidas = Tarea.objects.filter(
        usuario=usuario,
        fecha_vencimiento__lt=tiempo_actual,
        estado__in=['pendiente', 'en_progreso']
    ).exclude(
        id__in=Notificacion.objects.filter(
            usuario=usuario,
            tipo='tarea_vencida',
            leida=False
        ).values_list('tarea_id', flat=True)
    )
    
    # Crear notificaciones para tareas próximas a vencer
    for tarea in tareas_proximas:
        Notificacion.objects.create(
            usuario=usuario,
            tipo='fecha_vencimiento',
            mensaje=f'La tarea "{tarea.titulo}" del tablero "{tarea.tablero.nombre}" vence en menos de 24 horas',
            tarea=tarea
        )
    
    # Crear notificaciones para tareas vencidas
    for tarea in tareas_vencidas:
        Notificacion.objects.create(
            usuario=usuario,
            tipo='tarea_vencida',
            mensaje=f'La tarea "{tarea.titulo}" del tablero "{tarea.tablero.nombre}" ha vencido y no fue completada',
            tarea=tarea
        )
    
    return len(tareas_proximas) + len(tareas_vencidas) 