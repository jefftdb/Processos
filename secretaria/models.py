from django.db import models
from endereco.models import Endereco

class Secretaria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    endereco = models.ForeignKey(Endereco,models.CASCADE,related_name='endereco_secretaria')

    def __str__(self):
        return self.nome