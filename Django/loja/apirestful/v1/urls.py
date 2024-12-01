from django.urls import path
from .views import ClienteView, BuscarClientePorIdView, BuscarClientePorNomeView, ExportarCSVCompletoView

urlpatterns = [
    path('clientes/', ClienteView.as_view(), name='clientes_list'),
    path('clientes/<int:pk>/', ClienteView.as_view(), name='cliente_detail'),

    path('clientes/<int:pk>/', BuscarClientePorIdView.as_view(), name='buscar_cliente_por_id'),
    path('clientes/nome/<str:nome>/', BuscarClientePorNomeView.as_view(), name='buscar_cliente_por_nome'),

    path('exportar-dados-completos/', ExportarCSVCompletoView.as_view(), name='exportar_csv_completo'),
]
