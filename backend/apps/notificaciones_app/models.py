from django.db import models
from apps.usuarios_app.models import Usuario
from apps.tareas_app.models import Tarea

class Notificacion(models.Model):
    TIPO_CHOICES = [
        ('tarea_completada', 'Tarea Completada'),
        ('fecha_vencimiento', 'Fecha de Vencimiento Próxima'),
        ('tarea_vencida', 'Tarea Vencida'),
    ]
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    mensaje = models.TextField()
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='notificaciones')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leida = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return f'Notificación para {self.usuario.username}: {self.tipo}'