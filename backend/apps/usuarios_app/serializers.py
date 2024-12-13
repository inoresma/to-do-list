from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'foto_perfil', 'biografia', 'fecha_registro', 'ultimo_acceso']
        read_only_fields = ['fecha_registro', 'ultimo_acceso'] 