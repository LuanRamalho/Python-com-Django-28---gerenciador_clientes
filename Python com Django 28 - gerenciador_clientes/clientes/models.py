from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.TextField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
