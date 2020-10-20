# -*- coding: UTF-8 -*-
from django.db import models

from sorl.thumbnail import ImageField

# Create your models here.
class OrgImplementador(models.Model):
	nombre = models.CharField(max_length=250)
	logo = 	ImageField(upload_to='organizaciones',blank=True,null=True)

	class Meta:
		verbose_name_plural = "Organizaciones implementador"
		verbose_name = "Oganización implementador"

	def __str__(self):
		return self.nombre

class Finaciadores(models.Model):
	nombre = models.CharField(max_length=250)
	logo = 	ImageField(upload_to='finaciadores',blank=True,null=True)

	class Meta:
		verbose_name_plural = "Finaciadores"
		verbose_name = "Finaciador"

	def __str__(self):
		return self.nombre

class Aliados(models.Model):
	nombre = models.CharField(max_length=250)
	logo = 	ImageField(upload_to='aliados',blank=True,null=True)

	class Meta:
		verbose_name_plural = "Aliados"
		verbose_name = "Aliado"

	def __str__(self):
		return self.nombre

class Pais(models.Model):
	nombre = models.CharField(max_length=250)

	class Meta:
		verbose_name_plural = "Países metas"
		verbose_name = "País meta"

	def __str__(self):
		return self.nombre

class OrgSocias(models.Model):
	nombre = models.CharField(max_length=250)
	logo = 	ImageField(upload_to='org-socias',blank=True,null=True)
	pais =  models.ForeignKey(Pais,on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Organizaciones socias"
		verbose_name = "Oganización socia"

	def __str__(self):
		return self.nombre

class ActoresPOA(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Actores POA"
		verbose_name = "Actor POA"

class ProyectoFinanciado(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Proyectos Financiados"
		verbose_name = "Proyecto Financiado"
