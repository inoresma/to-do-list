from django.db import models
from apps.usuarios_app.models import Usuario
from apps.categorias_app.models import Categoria

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]
    
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='media')
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='pendiente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='tareas')
    completada = models.BooleanField(default=False)
    tablero = models.ForeignKey('tableros_app.Tablero', 
                              on_delete=models.CASCADE, 
                              related_name='tareas', 
                              null=True)
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return self.titulo