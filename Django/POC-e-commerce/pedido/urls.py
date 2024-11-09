from django.urls import path
from . import views


app_name = "pedido"


urlpatterns = [
    path('pagar/', views.Pagar.as_view(), name="pagar"),
    path('salvarpedido/', views.SalvarPedido.as_view(), name="salvarpedido"),
    path('detalhepedido/', views.DetalhePedido.as_view(), name="detalhepedido"),

]