from django.db import models
from arcondicionados.models import Arcondicionado

# Create your models here.

class Servico(models.Model):
    local = models.TextField('Local', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    arcondicionado = models.TextField('Ar-Condicionado', max_length=100) 
    tecnico = models.TextField('Tecnico', max_length=50)
    
    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.descricao