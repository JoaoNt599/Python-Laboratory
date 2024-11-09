from django.db import models
from django.urls import reverse
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self) :
        return self.nome
    
    def get_absolute_url(self):
        return reverse('main:listar_produtos_por_categoria', args=[self.slug])
    

class Produto(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='produtos/%Y/%m/%d', blank=True)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('main:detalhes_produto', args=[self.id, self.slug])
    











