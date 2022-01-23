from django.db import models


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=16)
    cep = models.CharField(max_length=12)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=20)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "paciente"

    def __str__(self) -> str:
        return self.nome
