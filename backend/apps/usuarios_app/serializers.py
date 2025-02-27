from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.conf import settings
import re

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    foto_perfil = serializers.ImageField(required=False)
    
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'first_name', 
                 'last_name', 'foto_perfil', 'biografia', 'fecha_registro', 
                 'ultimo_acceso']
        read_only_fields = ['fecha_registro', 'ultimo_acceso']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {
                'error_messages': {
                    'unique': 'Este nombre de usuario ya está siendo utilizado.',
                    'invalid': 'El nombre de usuario contiene caracteres inválidos.'
                }
            },
            'email': {
                'error_messages': {
                    'unique': 'Este correo electrónico ya está registrado.',
                    'invalid': 'Por favor ingrese un correo electrónico válido.'
                }
            }
        }
        
        # Documentación de campos
        swagger_schema_fields = {
            'description': 'Serializer para el modelo Usuario',
            'properties': {
                'username': {
                    'type': 'string',
                    'description': 'Nombre de usuario único',
                    'max_length': 150
                },
                'email': {
                    'type': 'string',
                    'format': 'email',
                    'description': 'Correo electrónico del usuario'
                },
                'password': {
                    'type': 'string',
                    'format': 'password',
                    'description': 'Contraseña del usuario (solo escritura)',
                    'write_only': True
                },
                'first_name': {
                    'type': 'string',
                    'description': 'Nombre del usuario',
                    'max_length': 150
                },
                'last_name': {
                    'type': 'string',
                    'description': 'Apellido del usuario',
                    'max_length': 150
                },
                'foto_perfil': {
                    'type': 'string',
                    'format': 'binary',
                    'description': 'Imagen de perfil del usuario'
                },
                'biografia': {
                    'type': 'string',
                    'description': 'Biografía o descripción del usuario',
                    'max_length': 500
                },
                'fecha_registro': {
                    'type': 'string',
                    'format': 'date-time',
                    'description': 'Fecha de registro del usuario',
                    'read_only': True
                },
                'ultimo_acceso': {
                    'type': 'string',
                    'format': 'date-time',
                    'description': 'Última vez que el usuario accedió',
                    'read_only': True
                }
            }
        } 
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres."
            )
        
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "La contraseña debe incluir al menos una letra mayúscula."
            )
            
        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError(
                "La contraseña debe incluir al menos un número."
            )
            
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|]', value):
            raise serializers.ValidationError(
                "La contraseña debe incluir al menos un carácter especial."
            )
            
        return value
        
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret['foto_perfil']:
            # Asegurarse de que la URL sea absoluta
            if not ret['foto_perfil'].startswith('http'):
                request = self.context.get('request')
                if request:
                    # Usar el host de la solicitud actual para construir la URL
                    host = request.get_host()
                    # Siempre reemplazar 'backend' por 'localhost' para acceso desde el navegador
                    if 'backend' in host:
                        host = host.replace('backend', 'localhost')
                    protocol = 'https' if request.is_secure() else 'http'
                    ret['foto_perfil'] = f"{protocol}://{host}{settings.MEDIA_URL}{ret['foto_perfil']}"
                else:
                    # Fallback a localhost si no hay solicitud
                    ret['foto_perfil'] = f"http://localhost:8000{settings.MEDIA_URL}{ret['foto_perfil']}"
            # También reemplazar 'backend' por 'localhost' si ya es una URL completa
            elif 'backend' in ret['foto_perfil']:
                ret['foto_perfil'] = ret['foto_perfil'].replace('backend', 'localhost')
        return ret 