from django.db import models
from listas.models import *
from modulo_gerencia.models import *
from django.contrib.auth.models import User

# Create your models here.
class Contrapartida(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Contrapartida'
        verbose_name = 'Contrapartida'

class InlineContrapartida(models.Model):
    contrapartida = models.ForeignKey(Contrapartida, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(OrgImplementador, on_delete=models.CASCADE)
    costos_admin = models.FloatField(verbose_name='Aporte a Costos Administrativos')
    salario_programatico = models.FloatField(verbose_name='Aporte a Salario Programático')
    aporte_actividades = models.FloatField(verbose_name='Aporte a actividades')
    overhead = models.FloatField(verbose_name='Aporte a Overhead')

    class Meta:
        verbose_name_plural = 'Contrapartida'
        verbose_name = 'Contrapartida'
