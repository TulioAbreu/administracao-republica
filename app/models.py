from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField(default=1)
    rank = models.CharField(max_length=1, default=1)

    def get_rank(self):
        if str(self.rank) == '1':
            return "Bixo"
        elif str(self.rank) == '2':
            return "Semi-Bicho"
        elif str(self.rank) == '3':
            return "Moradora"
        elif str(self.rank) == '4':
            return "Semi-Decana"
        elif str(self.rank) == '5':
            return "Decana"

    def __str__(self):
        return self.email


class Caixa(models.Model):
    mes = models.IntegerField(default=1)
    def __str__(self):
        if self.mes == 1:
            return "Janeiro"
        elif self.mes == 2:
            return "Fevereiro"
        elif self.mes == 3:
            return "Março"
        elif self.mes == 4:
            return "Abril"
        elif self.mes == 5:
            return "Maio"
        elif self.mes == 6:
            return "Junho"
        elif self.mes == 7:
            return "Julho"
        elif self.mes == 8:
            return "Agosto"
        elif self.mes == 9:
            return "Setembro"
        elif self.mes == 10:
            return "Outubro"
        elif self.mes == 11:
            return "Novembro"
        elif self.mes == 12:
            return "Dezembro"
        else:
            return "Null"

class Conta(models.Model):
    mes = models.ForeignKey("Caixa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=0.0)
    setPaid = models.BooleanField(verbose_name="Paga", default=False)
    # vencimento = models.DateTimeField()

    def paid(self):
        self.setPaid = True


