from django.contrib import admin
from .models import Empresa, Funcionario, Departamento

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
