from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.middleware.csrf import get_token
from .serializers import UsuarioSerializer
from rest_framework.permissions import AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [permissions.IsAuthenticated()]
    
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

@api_view(['POST'])
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message': 'Sesión cerrada correctamente'})
    return Response({'message': 'No hay sesión activa'}, status=status.HTTP_400_BAD_REQUEST)

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
        return Response({
            'detail': 'Login exitoso',
            'csrftoken': get_token(request)
        })
    else:
        return Response(
            {'detail': 'Credenciales inválidas'}, 
            status=status.HTTP_401_UNAUTHORIZED
        )
