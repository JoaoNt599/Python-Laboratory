from django.db import models
from django.contrib.auth.models import AbstractUser


class Editora(models.Model):
    nome = models.CharField(max_length=100)


class Livro(models.Model):
    titulo = models.CharField(max_length=250)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='capas/')


class Usuario(AbstractUser):
    is_admin = models.BooleanField(default=False)

    class Meta:
        swappable = 'AUTH_USER_MODEL'


