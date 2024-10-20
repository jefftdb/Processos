from django.db import models

class Processo(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=45)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.numero