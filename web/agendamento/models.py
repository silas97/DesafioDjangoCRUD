from django.db import models

from medico.models import User
from paciente.models import Paciente

STATUS_CHOICES = [
    ('A Confirmar', "A Confirmar"),
    ('Confirmado', "Confirmado"),
    ('Finalizado', "Finalizado"),
]


class Agendamento(models.Model):
    data = models.DateTimeField()
    descricao = models.TextField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    pais = models.CharField(max_length=20)
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        db_table = "agendamento"
