from django.db import models
from modulo_gerencia.models import *
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey
# Create your models here.

class IndObjetivos(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	objetivo = ChainedForeignKey(Objetivo,
								chained_field="proyecto",
        						chained_model_field="proyecto",)
	indicador = ChainedForeignKey(IndicadoresObjetivos,
								chained_field="objetivo",
        						chained_model_field="objetivo",)

	class Meta:
		verbose_name_plural = "Indicadores de Objetivos"
		verbose_name = "Indicadores de Objetivo"

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
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
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
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
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
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
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
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
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
		verbose_name_plural = "Indicadores de Efectos"
		verbose_name = "Indicadores de Efectos"

	def __str__(self):
		return '%s' % (self.indicador)


class IndEfecto1_1(models.Model):
	obj = models.ForeignKey(IndEfectos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_productores = models.IntegerField('Número de productores adoptando BPA',null=True,blank=True)
	porcentaje_mujeres = models.IntegerField('% de mujeres adoptando BPA',null=True,blank=True)
	porentaje_jovenes = models.IntegerField('% de Jovenes adoptando BPA',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-efecto-1-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.1"
		verbose_name = "Indicador 1.1"

class IndEfecto1_2(models.Model):
	obj = models.ForeignKey(IndEfectos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_empresas = models.IntegerField('Número de empresas implementando MNC',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-efecto-1-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2"
		verbose_name = "Indicador 1.2"

class IndEfecto2_1(models.Model):
	obj = models.ForeignKey(IndEfectos,on_delete=models.CASCADE) 
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	nombre_politica = models.CharField(max_length=300,verbose_name='Nombre de Pólitica/Estrategia actualizada',null=True,blank=True)
	descripcion = models.TextField(null=True,blank=True)
	estado_esfuerzo = models.CharField(max_length=100,choices=ESTADO_ESFUERZO_CHOICES,verbose_name='Estado de esfuerzo',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-efecto-2-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2.1"
		verbose_name = "Indicador 2.1"

#Productos
class IndProductos(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	producto = ChainedForeignKey(Producto,
								chained_field="proyecto",
        						chained_model_field="proyecto",)
	indicador = ChainedForeignKey(IndicadoresProductos,
								chained_field="producto",
        						chained_model_field="producto",)

	class Meta:
		verbose_name_plural = "Indicadores de Productos"
		verbose_name = "Indicadores de Productos"

	def __str__(self):
		return '%s' % (self.indicador)

class IndProducto1_1_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-1-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.1.1"
		verbose_name = "Indicador 1.1.1"

class IndProducto1_1_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True)
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-1-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.1.2"
		verbose_name = "Indicador 1.1.2"
	
class IndProducto1_1_3(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_comunidades = models.IntegerField('Número de comunidades de práctica en marcha',null=True,blank=True)
	numero_fincas = models.IntegerField('Número de fincas pilotos en marcha',null=True,blank=True)
	numero_negocios = models.IntegerField('Número de negocios inclusivos en marcha',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-1-3/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.1.3"
		verbose_name = "Indicador 1.1.3"
	
class IndProducto1_2_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_iniciativas = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-2-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2.1"
		verbose_name = "Indicador 1.2.1"
	
class IndProducto1_2_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_iniciativas = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-2-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2.2"
		verbose_name = "Indicador 1.2.2"

class IndProducto1_2_3(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_modelos = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-2-3/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2.3"
		verbose_name = "Indicador 1.2.3"

class IndProducto1_2_4(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_ofertas = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-2-4/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2.4"
		verbose_name = "Indicador 1.2.4"

class IndProducto1_2_5(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_estudio = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-2-5/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.2.5"
		verbose_name = "Indicador 1.2.5"
	
class IndProducto1_3_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_participantes = models.IntegerField(verbose_name='Número de participantes ',null=True,blank=True)
	numero_eventos = models.IntegerField(verbose_name='Numero de eventos o iniciativas',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-3-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.3.1"
		verbose_name = "Indicador 1.3.1"

class IndProducto1_3_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_experiencias = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-3-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.3.2"
		verbose_name = "Indicador 1.3.2"

class IndProducto1_3_3(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_actores = models.IntegerField(verbose_name='Número de actores',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-3-3/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.3.3"
		verbose_name = "Indicador 1.3.3"
	
class IndProducto1_4_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_documentos = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-4-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.4.1"
		verbose_name = "Indicador 1.4.1"

class IndProducto1_4_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_documentos = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-4-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.4.2"
		verbose_name = "Indicador 1.4.2"

class IndProducto1_4_3(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_documentos = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-4-3/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.4.3"
		verbose_name = "Indicador 1.4.3"

class IndProducto1_4_4(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_estudio = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-1-4-4/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 1.4.4"
		verbose_name = "Indicador 1.4.4"

class IndProducto2_5_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_comite = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-2-5-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2.5.1"
		verbose_name = "Indicador 2.5.1"

class IndProducto2_5_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_plataformas = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-2-5-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2.5.2"
		verbose_name = "Indicador 2.5.2"

class IndProducto2_6_1(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_politica = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-2-6-1/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2.6.1"
		verbose_name = "Indicador 2.6.1"

class IndProducto2_6_2(models.Model):
	producto = models.ForeignKey(IndProductos, on_delete=models.CASCADE)
	anio = models.IntegerField('Año')
	semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
	numero_politica = models.IntegerField(verbose_name='Número',null=True,blank=True)
	fuente = models.CharField(max_length=300,null=True,blank=True,verbose_name='Título y fuente')
	url = models.URLField(null=True,blank=True)
	archivo = models.FileField(upload_to='ind-prod-2-6-2/',null=True,blank=True)

	class Meta:
		verbose_name_plural = "Indicador 2.6.2"
		verbose_name = "Indicador 2.6.2"