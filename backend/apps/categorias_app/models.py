from django.db import models
from apps.usuarios_app.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    color = models.CharField(max_length=7, default="#000000")  # Para guardar códigos HEX de colores
    icono = models.CharField(max_length=50, blank=True)  # Para guardar nombres de iconos
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='categorias')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre