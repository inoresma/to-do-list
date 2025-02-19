from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableroViewSet

router = DefaultRouter()
router.register(r'tableros', TableroViewSet, basename='tablero')

urlpatterns = [
    path('', include(router.urls)),
] 