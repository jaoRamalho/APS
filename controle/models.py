from django.db import models

class PontoDeAcesso(models.Model):

    PLANOS = [
    ("10", "10 megas"),
    ("10F", "10 Megas Fibre"),
    ("100", "100 Megas"),
    ("100F", "100 Megas Fibra"),
    ("500", "500 Megas"),
    ("500F", "500 Megas Fibra"),
    ]

    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20)
    data_instalacao = models.DateTimeField()
    data_cancelamento = models.DateTimeField(null=True)
    endereco = models.TextField()
    plano = models.CharField(max_length=4, choices=PLANOS, default=10)
    status = models.BooleanField(default=True)

class Cliente(models.Model):
    
    nome = models.CharField(max_length=100)
    telefone = models.TextField(max_length=100)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_vencimento = models.DateTimeField()
    

