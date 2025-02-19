from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Tarea
from .serializers import TareaSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.

class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Tarea.objects.filter(usuario=self.request.user)
        tablero_id = self.request.query_params.get('tablero', None)
        if tablero_id is not None:
            queryset = queryset.filter(tablero_id=tablero_id)
        return queryset
    
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
