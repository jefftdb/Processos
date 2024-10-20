from django.contrib import admin
from funcionario.models import Funcionario

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','cpf', 'telefone','data_nascimento','foto')
    search_fields = ('cpf','telefone','secretarias','processos','email')


admin.site.register(Funcionario,FuncionarioAdmin)
