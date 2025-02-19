from rest_framework import serializers
from .models import Notificacion
from apps.tareas_app.serializers import TareaSerializer

class NotificacionSerializer(serializers.ModelSerializer):
    tarea = TareaSerializer(read_only=True)
    
    class Meta:
        model = Notificacion
        fields = ['id', 'tipo', 'mensaje', 'tarea', 'fecha_creacion', 'leida']
        read_only_fields = ['fecha_creacion'] 