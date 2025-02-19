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
        
        # Documentación de campos
        swagger_schema_fields = {
            'description': 'Serializer para el modelo Tarea',
            'properties': {
                'titulo': {
                    'type': 'string',
                    'description': 'Título de la tarea',
                    'max_length': 200
                },
                'descripcion': {
                    'type': 'string',
                    'description': 'Descripción detallada de la tarea'
                },
                'fecha_vencimiento': {
                    'type': 'string',
                    'format': 'date-time',
                    'description': 'Fecha y hora de vencimiento de la tarea'
                },
                'prioridad': {
                    'type': 'string',
                    'enum': ['baja', 'media', 'alta'],
                    'description': 'Nivel de prioridad de la tarea'
                },
                'estado': {
                    'type': 'string',
                    'enum': ['pendiente', 'en_progreso', 'completada'],
                    'description': 'Estado actual de la tarea'
                }
            }
        } 