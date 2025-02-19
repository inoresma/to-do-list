from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Tarea
from .serializers import TareaSerializer
import logging
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

logger = logging.getLogger(__name__)

# Create your views here.

@extend_schema(tags=['tareas'])
class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Tarea.objects.filter(usuario=self.request.user)
        tablero_id = self.request.query_params.get('tablero', None)
        if tablero_id is not None:
            queryset = queryset.filter(tablero_id=tablero_id)
        return queryset
    
    @extend_schema(
        summary="Listar tareas",
        description="Obtiene la lista de tareas del usuario autenticado",
        parameters=[
            OpenApiParameter(
                name='tablero',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='ID del tablero para filtrar tareas'
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Crear tarea",
        description="Crea una nueva tarea asociada al usuario autenticado"
    )
    def create(self, request, *args, **kwargs):
        logger.info(f"Datos recibidos: {request.data}")
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            logger.error(f"Errores de validación: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error al crear tarea: {str(e)}")
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
