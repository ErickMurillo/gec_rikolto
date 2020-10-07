# -*- coding: UTF-8 -*-
from django.db import models
from listas.models import * 
from smart_selects.db_fields import ChainedManyToManyField, ChainedForeignKey

# Create your models here.

class Proyecto(models.Model):
	nombre = models.CharField(max_length=250)
	org_implementador = models.ForeignKey(OrgImplementador,on_delete=models.CASCADE,verbose_name='Oganización implementador')
	financiadores = models.ManyToManyField(Finaciadores)
	anio_inicio = models.DateField()
	anio_fin = models.DateField()
	aliados = models.ManyToManyField(Aliados)
	paises = models.ManyToManyField(Pais,verbose_name='Países metas')
	org_socias = ChainedManyToManyField(OrgSocias,
										chained_field="paises",
        								chained_model_field="pais",
        								horizontal=True,
        								verbose_name='Organizaciones socias clave por país')

	class Meta:
		verbose_name_plural = "Proyectos"
		verbose_name = "Proyecto"

	def __str__(self):
		return self.nombre


class Objetivo(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField("Descripción de objetivo")

	class Meta:
		verbose_name_plural = "Objetivos"
		verbose_name = "Objetivo"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)

class IndicadoresObjetivos(models.Model):
	objetivo = models.ForeignKey(Objetivo,on_delete=models.CASCADE) 
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Indicadores objetivos"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)

class Efecto(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	objetivo = ChainedForeignKey(Objetivo,
								chained_field="proyecto",
        						chained_model_field="proyecto",) 
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Efectos"
		verbose_name = "Efecto"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)

class IndicadoresEfectos(models.Model):
	efecto = models.ForeignKey(Efecto,on_delete=models.CASCADE) 
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Indicadores efectos"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)


class Producto(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	efecto = ChainedForeignKey(Efecto,
								chained_field="proyecto",
        						chained_model_field="proyecto",) 
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Productos"
		verbose_name = "Producto"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)

class IndicadoresProductos(models.Model):
	producto = models.ForeignKey(Producto,on_delete=models.CASCADE) 
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Indicadores productos"

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)

class Actividades(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE)
	producto = ChainedForeignKey(Producto,
								chained_field="proyecto",
        						chained_model_field="proyecto",)
	identificador = models.CharField(max_length=20)
	descripcion = models.TextField()

	class Meta:
		verbose_name_plural = "Actividades"
		verbose_name = "Actividad"
		# ordering = ['identificador']

	def __str__(self):
		return '%s - %s' % (self.identificador,self.descripcion)
