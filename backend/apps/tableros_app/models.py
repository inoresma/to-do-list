from django.db import models
from apps.usuarios_app.models import Usuario

class Tablero(models.Model):
    ICONOS_CHOICES = [
        ('clipboard', 'Lista'),
        ('calendar', 'Calendario'),
        ('star', 'Estrella'),
        ('heart', 'Corazón'),
        ('home', 'Casa'),
        ('book', 'Libro'),
        ('briefcase', 'Maletín'),
        ('academic-cap', 'Graduación'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tableros')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=7, default='#4F46E5')  # Color en formato HEX
    icono = models.CharField(max_length=20, choices=ICONOS_CHOICES, default='clipboard')
    
    class Meta:
        verbose_name = 'Tablero'
        verbose_name_plural = 'Tableros'
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return self.nombre

    @property
    def tareas_count(self):
        return self.tareas.count()