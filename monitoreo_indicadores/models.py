from django.db import models
from modulo_gerencia.models import *
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey
# Create your models here.

class IndObjetivos(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	indicador = ChainedForeignKey(IndicadoresObjetivos,
								chained_field="proyecto",
        						chained_model_field="objetivo",)

	class Meta:
		verbose_name_plural = "Objetivos"
		verbose_name = "Objetivo"

	def __str__(self):
		return '%s' % (self.indicador)

SEMESTRE_CHOICES = ((1,'I'),(2,'II'))

class ObjInd1(models.Model):
	obj = models.ForeignKey(IndObjetivos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_productores = models.IntegerField('Número de productores',null=True,blank=True)
	ingreso_saf = models.FloatField('Ingreso de SAF USD/ha',null=True,blank=True)
	aumento_ingreso_saf = models.FloatField('Aumento de Ingreso SAF (%)',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='obj-indicador-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1"
		verbose_name = "Indicador 1"

class ObjInd2(models.Model):
	obj = models.ForeignKey(IndObjetivos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_productores = models.IntegerField('Número de productores',null=True,blank=True)
	productividad_cacao = models.FloatField('Productividad cacao kg/ha',null=True,blank=True)
	aumento_productividad_cacao = models.FloatField('Aumento de productividad (%)',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='obj-indicador-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2"
		verbose_name = "Indicador 2"

ESTADO_ESFUERZO_CHOICES = (('No iniciado','No iniciado'),('Iniciado','Iniciado'),
							('Avanzado','Avanzado'),('Cumplido','Cumplido'))

class ObjInd3(models.Model):
	obj = models.ForeignKey(IndObjetivos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	nombre_politica_regional = models.CharField(max_length=250, verbose_name='Nombre de Pólitica Regional',null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	estado_esfuerzo = models.CharField(max_length=100,choices=ESTADO_ESFUERZO_CHOICES,verbose_name='Estado de esfuerzo',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='obj-indicador-3/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 3"
		verbose_name = "Indicador 3"

class ObjInd4(models.Model):
	obj = models.ForeignKey(IndObjetivos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	nombre_plataforma = models.CharField(max_length=250, verbose_name='Nombre de Plataforma',null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	estado_plataforma = models.CharField(max_length=100,choices=ESTADO_ESFUERZO_CHOICES,verbose_name='Estado de Plataforma',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='obj-indicador-4/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 4"
		verbose_name = "Indicador 4"

#efectos -----------------------------------------------------------------
class IndEfectos(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	efecto = ChainedForeignKey(Efecto,
								chained_field="proyecto",
        						chained_model_field="proyecto",)
	indicador = ChainedForeignKey(IndicadoresEfectos,
								chained_field="efecto",
        						chained_model_field="efecto",)

	class Meta:
		verbose_name_plural = "Efectos"
		verbose_name = "Efectos"

	def __str__(self):
		return '%s' % (self.indicador)


class IndEfecto1_1(models.Model):
	obj = models.ForeignKey(IndEfectos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_productores = models.IntegerField('Número de productores adoptando BPA',null=True,blank=True)
	porcentaje_mujeres = models.IntegerField('% de mujeres adoptando BPA',null=True,blank=True)
	porentaje_jovenes = models.IntegerField('% de Jovenes adoptando BPA',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='ind-efecto-1-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.1"
		verbose_name = "Indicador 1.1"

class IndEfecto1_2(models.Model):
	obj = models.ForeignKey(IndEfectos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_empresas = models.IntegerField('Número de empresas implementando MNC',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	archivo = models.FileField(upload_to='ind-efecto-1-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2"
		verbose_name = "Indicador 1.2"