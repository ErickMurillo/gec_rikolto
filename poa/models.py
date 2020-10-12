from django.db import models
from modulo_gerencia.models import *
from listas.models import *

# Create your models here.
class Poa(models.Model):
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
	anio = models.IntegerField(verbose_name="Año", unique=True)

	def __str__(self):
		return str(self.anio)
	
	class Meta:
		verbose_name_plural = 'POA'
		verbose_name = 'POA'

class IndicadoresPOA(models.Model):
	poa = models.ForeignKey(Poa, on_delete=models.CASCADE)
	indicador = models.ForeignKey(Actividades, on_delete=models.CASCADE)
	semestre_1 = models.BooleanField()
	semestre_2 = models.BooleanField()
	monto_presupuestado = models.FloatField()
	monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado al final de I semestre',blank=True,null=True)
	monto_final_anio = models.FloatField(verbose_name='Monto ejecutado al final del año',blank=True,null=True)
	actores = models.ManyToManyField(ActoresPOA)
	fecha_finalizacion = models.DateField()

	class Meta:
		verbose_name_plural = 'Actividades'
		verbose_name = 'Actividad'