from rest_framework import serializers
from .models import Tablero

class TableroSerializer(serializers.ModelSerializer):
    tareas_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Tablero
        fields = ['id', 'nombre', 'descripcion', 'usuario', 
                 'fecha_creacion', 'tareas_count', 'color', 'icono']
        read_only_fields = ['fecha_creacion', 'usuario']