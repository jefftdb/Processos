from django.contrib import admin
from endereco.models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua','estado','cep','bairro','pais','numero')
    search_fields = ('funcionario','cep')

admin.site.register(Endereco,EnderecoAdmin)
