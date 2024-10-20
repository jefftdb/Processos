from django.db import models


class Endereco(models.Model):
    id      = models.AutoField(primary_key=True)
    rua     = models.CharField(max_length=100)
    cidade  = models.CharField(max_length=50)
    estado  = models.CharField(max_length=50)
    cep     = models.CharField(max_length= 20)
    bairro  = models.CharField(max_length= 20)
    pais = models.CharField(max_length= 20)
    numero  = models.CharField(max_length= 6)
    

    def __str__(self):
        return f'''Rua:{self.rua} Nº:{self.numero} CEP:{self.cep}
                    Pais:{self.pais} Estado:{self.estado}
                    Cidade:{self.cidade} Bairro:{self.bairro}'''
