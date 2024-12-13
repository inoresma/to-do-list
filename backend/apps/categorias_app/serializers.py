from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'color', 'icono', 
                 'usuario', 'fecha_creacion']
        read_only_fields = ['fecha_creacion'] 