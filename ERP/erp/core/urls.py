from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet


router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
