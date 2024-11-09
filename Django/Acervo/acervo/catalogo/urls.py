# catalogo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    # path('adicionar-livro/', views.adicionar_livro, name='adicionar_livro'),
    # path('adicionar-editora/', views.adicionar_editora, name='adicionar_editora'),
    # path('adicionar-usuario/', views.adicionar_usuario, name='adicionar_usuario'),
]
