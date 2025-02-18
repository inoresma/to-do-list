from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from . import views

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 