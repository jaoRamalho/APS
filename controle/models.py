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

    PLANOS = [
    ("10", "10 megas"),
    ("10F", "10 Megas Fibre"),
    ("100", "100 Megas"),
    ("100F", "100 Megas Fibra"),
    ("500", "500 Megas"),
    ("500F", "500 Megas Fibra"),
    ]


    
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    telefone = models.TextField(max_length=100)
    endereco = models.TextField()
    plano = models.CharField(max_length=4, choices=PLANOS, default=10)
    devendo = models.BooleanField(default=False)


    def __str__(self):
        return self.nome

class Conta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_vencimento = models.DateTimeField()


class OrdemDeServico(models.Model):
    TIPOS_OS = [
    ("10", "10 megas"),
    ("500F", "500 Megas Fibra"),
    ]

    TIPOS_PRIORIDADE = [
    ("10", "10 megas"),
    ("500F", "500 Megas Fibra"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=4, choices=TIPOS_OS)
    prioridade = models.CharField(max_length=4, choices=TIPOS_PRIORIDADE)
    

from django.contrib.auth.models import User

class Equipe(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class PaginaAcesso(models.Model):
    nome_pagina = models.CharField(max_length=100)
    equipes = models.ManyToManyField(Equipe)

    def __str__(self):
        return self.nome_pagina

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.equipe.nome}"
