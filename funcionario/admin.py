from django.contrib import admin
from funcionario.models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'telefone','data_nascimento')
    search_fields = ('cpf','telefone','secretarias','processos')


admin.site.register(Funcionario,FuncionarioAdmin)
