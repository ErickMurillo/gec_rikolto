from django.db import models
from modulo_gerencia.models import *
from listas.models import *
from django.contrib.auth.models import User

# Create your models here.
class Viajes(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Movilización'
        verbose_name = 'Movilización'

SEMESTRE_CHOICES = (('I','I'),('II','II'))

class InlineViaje(models.Model):
    viaje = models.ForeignKey(Viajes, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    semestre = models.CharField(max_length=2,choices=SEMESTRE_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    personas_viajan = models.ManyToManyField(PersonasViajan)
    paises_viajan = models.ManyToManyField(Pais)
    gastos_boletos = models.FloatField()
    gastos_combustibles = models.FloatField()
    gastos_alojamiento = models.FloatField()
    gastos_diarios = models.FloatField()
    otros_gastos = models.FloatField()
    archivo = models.FileField(upload_to='viajes/',null=True,blank=True,verbose_name='Informe de Viaje')

    class Meta:
        verbose_name_plural = 'Viajes'
        verbose_name = 'Viaje'
