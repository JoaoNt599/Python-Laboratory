from django.urls import path
from .views import ClienteView

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteView.as_view(), name='cliente-detail'),
]
