from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'Fotogradia [nome = {self.nome}]'

'''
para que o modelo funcione é necessário executar o comanando a seguir no terminal
pyhton manage.py makemigrations

'''