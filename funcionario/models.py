from django.db import models
from django.contrib.auth.models import User
from processo.models import Processo
from endereco.models import Endereco
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


class Funcionario(User):   
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateTimeField()
    secretarias = models.ManyToManyField('secretaria.Secretaria',related_name='secretarias_funcionarios')
    processos = models.ManyToManyField(Processo, related_name='processos_funcionario')
    endereco = models.ManyToManyField(Endereco,related_name='enderecos_funcionario')
    foto = models.ImageField(upload_to = 'funcionario/',blank = True, null =True)

    def __str__(self):
        return self.first_name

@receiver(post_delete, sender=Funcionario)
def deletar_foto_funcionario(sender, instance, **kwargs):
    # Verifica se a instância possui uma foto
    if instance.foto:
        # Se a foto existir no sistema de arquivos, ela será removida
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)