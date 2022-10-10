from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=false, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_jength=9)
    celula = models.CharField(max_length=14)
    ativo = models.BooleanField()
    
    def __str__(self):
        return self.nome
