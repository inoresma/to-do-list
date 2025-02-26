from rest_framework import serializers
from django.contrib.auth import get_user_model

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
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