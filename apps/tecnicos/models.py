from django.db import models
from arcondicionados.models import Arcondicionado

# Create your models here.

class Tecnico(models.Model):
    nome = models.TextField('Nome', max_length=100)
    registro = models.TextField('Registro', max_length=100)
    avaliacao = models.TextField('Avaliacao', max_length=100) 
    especialidade = models.TextField('Especialidade', max_length=100)
   
    
    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'
        ordering =['id']

    def __str__(self):
        return self.name
                               