from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Tablero
from .serializers import TableroSerializer

# Create your views here.

class TableroViewSet(viewsets.ModelViewSet):
    serializer_class = TableroSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Tablero.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
