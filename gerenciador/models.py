from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    vencimento = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    status_pagamento = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(
        default=timezone.now, verbose_name="Data da criação")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome
