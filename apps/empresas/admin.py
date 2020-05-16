from django.contrib import admin
from .models import Empresa, Funcionario, Departamento
from .models import Documento, Registro_Hora_Extra

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Documento)
admin.site.register(Registro_Hora_Extra)
