from rest_framework import serializers
from .models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_creacion', 'usuario', 'tarea']
        read_only_fields = ['fecha_creacion', 'usuario'] 