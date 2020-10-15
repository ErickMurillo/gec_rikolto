from django.db import models
from modulo_gerencia.models import *
from listas.models import *
from multiselectfield import MultiSelectField


# Create your models here.
class Poa(models.Model):
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
	anio = models.IntegerField(verbose_name="Año")
	actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)

	# def __str__(self):
	# 	return '%s %s' % (str(self.anio),self.actividad)
	
	class Meta:
		verbose_name_plural = 'POA'
		verbose_name = 'POA'

MESES_CHOICES = (('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),
                ('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),
                ('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),
                ('Diciembre','Diciembre'))

class IndicadoresPOA(models.Model):
	poa = models.ForeignKey(Poa, on_delete=models.CASCADE)
	identificador = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=250)
	semestre_1 = models.BooleanField()
	semestre_2 = models.BooleanField()
	monto_presupuestado = models.FloatField()
	monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado al final de I semestre',blank=True,null=True)
	monto_final_anio = models.FloatField(verbose_name='Monto ejecutado al final del año',blank=True,null=True)
	insumos = models.CharField(max_length=250,blank=True,null=True)
	actores = models.CharField(max_length=250,blank=True,null=True)
	responsable = models.CharField(max_length=250,blank=True,null=True)
	meses = MultiSelectField(choices=MESES_CHOICES)
	meses_ejecucion = MultiSelectField(choices=MESES_CHOICES,blank=True,null=True)

	class Meta:
		verbose_name_plural = 'Sub Actividades'
		verbose_name = 'Sub Actividad'
		