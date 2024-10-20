from django.contrib import admin
from processo.models import Processo

class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'descricao')
    search_fields = ('numero', 'descricao')

admin.site.register(Processo,ProcessoAdmin)
