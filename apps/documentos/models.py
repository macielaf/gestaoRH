from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey\
        (Funcionario, on_delete=models.SET_NULL, blank=True, null=True) # set_null caso exclua o documento nao exclui o funcionario

    def __str__(self):
        return self.descricao
