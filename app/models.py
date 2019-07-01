from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
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
