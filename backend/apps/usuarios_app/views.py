from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.middleware.csrf import get_token
from .serializers import UsuarioSerializer
from rest_framework.permissions import AllowAny
from apps.tareas_app.utils import verificar_tareas_por_vencer
from apps.notificaciones_app.models import Notificacion
from drf_spectacular.utils import extend_schema, OpenApiResponse

@extend_schema(tags=['auth'])
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [permissions.IsAuthenticated()]
    
    @extend_schema(
        summary="Obtener perfil actual",
        description="Obtiene o actualiza la información del usuario autenticado",
        methods=['GET', 'PATCH']
    )
    @action(detail=False, methods=['get', 'patch'])
    def me(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        elif request.method == 'PATCH':
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(self.request.data.get('password'))
        user.save()

@extend_schema(
    tags=['auth'],
    summary="Cerrar sesión",
    description="Cierra la sesión del usuario actual",
    responses={200: OpenApiResponse(description="Logout exitoso")}
)
@api_view(['POST'])
def logout_view(request):
    # Eliminar notificaciones leídas del usuario antes de cerrar sesión
    Notificacion.objects.filter(
        usuario=request.user,
        leida=True
    ).delete()
    
    logout(request)
    return Response({'message': 'Logout exitoso'})

@extend_schema(
    tags=['auth'],
    summary="Iniciar sesión",
    description="Autentica al usuario y crea una sesión",
    request={
        'application/json': {
            'type': 'object',
            'properties': {
                'username': {'type': 'string'},
                'password': {'type': 'string', 'format': 'password'}
            },
            'required': ['username', 'password']
        }
    },
    responses={
        200: OpenApiResponse(description="Login exitoso"),
        400: OpenApiResponse(description="Credenciales inválidas")
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])  # Permite acceso sin autenticación
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'detail': 'Por favor proporcione usuario y contraseña'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        # Verificar tareas por vencer después del login
        tareas_proximas = verificar_tareas_por_vencer(user)
        
        return Response({
            'message': 'Login exitoso',
            'tareas_por_vencer': tareas_proximas
        })
    else:
        return Response({
            'error': 'Credenciales inválidas'
        }, status=status.HTTP_400_BAD_REQUEST)
