from rest_framework import serializers
from .models import Tablero

class TableroSerializer(serializers.ModelSerializer):
    tareas_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Tablero
        fields = ['id', 'nombre', 'descripcion', 'usuario', 
                 'fecha_creacion', 'tareas_count', 'color', 'icono']
        read_only_fields = ['fecha_creacion', 'usuario']
        
        # Documentación de campos
        swagger_schema_fields = {
            'description': 'Serializer para el modelo Tablero',
            'properties': {
                'nombre': {
                    'type': 'string',
                    'description': 'Nombre del tablero',
                    'max_length': 100
                },
                'descripcion': {
                    'type': 'string',
                    'description': 'Descripción del tablero'
                },
                'color': {
                    'type': 'string',
                    'description': 'Color del tablero en formato HEX',
                    'pattern': '^#[0-9A-Fa-f]{6}$',
                    'example': '#4F46E5'
                },
                'icono': {
                    'type': 'string',
                    'enum': ['clipboard', 'calendar', 'star', 'heart', 'home', 
                            'book', 'briefcase', 'academic-cap'],
                    'description': 'Icono que representa el tablero'
                },
                'tareas_count': {
                    'type': 'integer',
                    'description': 'Número total de tareas en el tablero',
                    'read_only': True
                }
            }
        }