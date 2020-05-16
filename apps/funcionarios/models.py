from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionario')
    user = models.OneToOneField(User, on_delete=models.PROTECT) # usa a biblioteca de user para gerar a chave/controlar
    departamentos = models.ManyToManyField(Departamento) # um funcionarios pode estar em varios departamentos
    empresas = models.ForeignKey(Empresa, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
