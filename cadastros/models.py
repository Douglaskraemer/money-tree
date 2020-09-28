from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    valor_total = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Valor total")
    vencimento = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    #opcoes = models.BooleanField(default=False, verbose_name="Opções")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} (R${})".format(self.descricao, self.valor_total)
