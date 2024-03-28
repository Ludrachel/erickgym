from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=250)
    idade = models.PositiveIntegerField(default=12)
    ativo = models.BooleanField(default=True)
 
