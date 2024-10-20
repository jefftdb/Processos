from django.contrib import admin
from secretaria.models import Secretaria

class SecretariaAdmin(admin.ModelAdmin):
    list_display = ('nome','endereco')
    search_fields = ('nome','endereco')

admin.site.register(Secretaria,SecretariaAdmin)
