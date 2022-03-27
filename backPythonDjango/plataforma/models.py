from django.db import models
from django.contrib.auth.models import User

class Parceiro(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nome

class TipoContrato(models.Model):
    nome = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nome        

class Acompanhamento(models.Model):
    nome = models.CharField(max_length=30)
    data = models.DateField()
    def __str__(self) -> str:
        return self.nome        

class Contrato(models.Model):
    numero = models.CharField(max_length=50)
    parceiro =models.ForeignKey(Parceiro, on_delete=models.CASCADE, null=True)
    tipoContrato =models.ForeignKey(TipoContrato, on_delete=models.CASCADE, null=True)
    dataCadastro = models.DateField(null=True, verbose_name="Data de Cadastro")    
    dataAssinatura = models.DateField(null=True, verbose_name="Data de assinatura")    
    objetivo = models.CharField(null=True,max_length=250)
    acompanhamento = models.ManyToManyField(Acompanhamento)
    def __str__(self) -> str:
        return self.numero

