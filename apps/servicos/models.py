from django.db import models
from arcondicionados.models import Arcondicionado
from tecnicos.models import Tecnico

# Create your models here.

class Servico(models.Model):
    local = models.TextField('Local', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    arcondicionado = models.ForeignKey(Arcondicionado, on_delete=models.CASCADE, verbose_name='Ar-Condicionado', null=True, blank=True)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name='Tecnico')
    
    
    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.descricao