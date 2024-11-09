from django.contrib import admin
from .models import Categoria, Produto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 
                    'slug', 
                    'preco', 
                    'estoque', 
                    'disponivel', 
                    'data_criacao', 
                    'data_ultima_atualizacao']
    list_filter = ['disponivel', 'data_criacao', 'data_ultima_atualizacao']
    list_editable = ['preco', 'estoque', 'disponivel']
    prepopulated_fields = {'slug': ('nome',)}