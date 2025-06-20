from django.db import models

# Create your models here.

class Arcondicionado(models.Model):
    marca = models.CharField('Marca', max_length=50)
    modelo = models.CharField('Modelo', max_length=50)
    capacidade = models.CharField('Capacidade', max_length=50)
    tecnologia = models.CharField('Tecnologia', max_length=50)

    class Meta:
        verbose_name = 'Arcondicionado'
        verbose_name_plural = 'Arcondicionados'
        ordering =['id']

    def __str__(self):
        return self.modelo