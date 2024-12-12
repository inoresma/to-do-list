from django.db import models
from apps.usuarios_app.models import Usuario
from apps.tareas_app.models import Tarea

class Comentario(models.Model):
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='comentarios')
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return f'Comentario de {self.usuario.username} en {self.tarea.titulo}'