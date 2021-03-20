from django.db import models
from apps.soporte.constants import ESTADOS_TICKETS

class Ticket(models.Model):

    titulo = models.CharField('Titulo', max_length=100)
    descripcion = models.CharField('Descripcion', max_length=100)
    estados = models.CharField(
        'Estados', choices=ESTADOS_TICKETS, max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
