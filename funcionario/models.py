from django.db import models
from django.contrib.auth.models import User
from processo.models import Processo
from endereco.models import Endereco

class Funcionario(User):   
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateTimeField()
    secretarias = models.ManyToManyField('secretaria.Secretaria',related_name='secretarias_funcionarios')
    processos = models.ManyToManyField(Processo, related_name='processos_funcionario')
    endereco = models.ManyToManyField(Endereco,related_name='enderecos_funcionario')

    def __str__(self):
        return self.first_name