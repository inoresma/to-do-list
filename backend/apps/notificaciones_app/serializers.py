from rest_framework import serializers
from .models import Notificacion

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = ['id', 'tipo', 'mensaje', 'tarea', 'fecha_creacion', 'leida', 'usuario']
        read_only_fields = ['fecha_creacion', 'usuario'] 