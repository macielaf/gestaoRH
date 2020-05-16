from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):
        return self.nome




