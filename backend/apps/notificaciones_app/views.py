from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notificacion
from apps.tareas_app.models import Tarea
from django.utils import timezone
from rest_framework import status
from .serializers import NotificacionSerializer

# Create your views here.

@api_view(['GET'])
def notificaciones_no_leidas(request):
    count = Notificacion.objects.filter(
        usuario=request.user,
        leida=False
    ).count()
    return Response({'count': count})

@api_view(['GET'])
def listar_notificaciones(request):
    notificaciones = Notificacion.objects.filter(usuario=request.user)
    serializer = NotificacionSerializer(notificaciones, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def marcar_notificacion_leida(request, pk):
    try:
        notificacion = Notificacion.objects.get(pk=pk, usuario=request.user)
        notificacion.delete()
        return Response(status=status.HTTP_200_OK)
    except Notificacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
