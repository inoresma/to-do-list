from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Tablero
from .serializers import TableroSerializer
from rest_framework.decorators import api_view

# Create your views here.

@extend_schema(tags=['tableros'])
class TableroViewSet(viewsets.ModelViewSet):
    serializer_class = TableroSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tablero.objects.filter(usuario=self.request.user)
    
    @extend_schema(
        summary="Listar tableros",
        description="Obtiene la lista de tableros del usuario autenticado"
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Crear tablero",
        description="Crea un nuevo tablero asociado al usuario autenticado"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(
        summary="Obtener tablero",
        description="Obtiene los detalles de un tablero específico"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        summary="Actualizar tablero",
        description="Actualiza todos los campos de un tablero existente"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(
        summary="Eliminar tablero",
        description="Elimina un tablero y todas sus tareas asociadas"
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
