from rest_framework import serializers
from .models import Tarea
from apps.tableros_app.models import Tablero

class TableroMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablero
        fields = ['id', 'nombre']

class TareaSerializer(serializers.ModelSerializer):
    tablero_info = TableroMiniSerializer(source='tablero', read_only=True)
    
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 
                 'fecha_vencimiento', 'prioridad', 'estado', 'usuario', 
                 'tablero', 'tablero_info']
        read_only_fields = ['fecha_creacion', 'usuario'] 