from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 
                 'fecha_vencimiento', 'prioridad', 'estado', 'usuario', 
                 'tablero']
        read_only_fields = ['fecha_creacion', 'usuario'] 