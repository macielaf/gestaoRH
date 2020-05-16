from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionario')

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome

class Documento(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Registro_Hora_Extra(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return self.motivo

