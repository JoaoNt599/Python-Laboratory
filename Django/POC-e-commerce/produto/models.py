from django.db import models
from django.conf import settings
from PIL import Image
import os
from django.utils.text import slugify
from utils import utils


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255, verbose_name='Descrição Curta')
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(default=0, verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(default=0, verbose_name='Preço Promo')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço'

    def __str__(self):
        return self.nome

    @staticmethod
    def resize_image(original_img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, original_img.name)
        img_pil = Image.open(img_full_path)

        original_width, original_height = img_pil.size
        new_height = round((new_width * original_height) / original_width)

        if new_height >= original_height:
            img_pil.close()
            return

        nova_imagem = img_pil.resize((new_width, new_height), Image.LANCZOS)
        nova_imagem.save(img_full_path, optimize=True, quality=60)
        img_pil.close()

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        img_max_width = 800

        if self.imagem:
            self.resize_image(self.imagem, img_max_width)


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField(default=0)
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.name

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
