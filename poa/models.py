from django.db import models
from modulo_gerencia.models import *
from listas.models import *
from multiselectfield import MultiSelectField

# Create your models here.
class Poa(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Plan de actividades'
        verbose_name = 'Plan de actividades'

MESES_CHOICES = (('Enero','Enero'),('Febrero','Febrero'),('Marzo','Marzo'),('Abril','Abril'),
                ('Mayo','Mayo'),('Junio','Junio'),('Julio','Julio'),('Agosto','Agosto'),
                ('Septiembre','Septiembre'),('Octubre','Octubre'),('Noviembre','Noviembre'),
                ('Diciembre','Diciembre'))

class ActividadesPOA(models.Model):
    poa = models.ForeignKey(Poa, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Actividades'
        verbose_name = 'Actividad'

class SubActividadesPOA(models.Model):
    actividad_poa = models.ForeignKey(ActividadesPOA, on_delete=models.CASCADE)
    identificador = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=250)
    semestre_1 = models.BooleanField()
    semestre_2 = models.BooleanField()
    monto_presupuestado = models.FloatField()
    monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado I semestre',blank=True,null=True)
    monto_final_anio = models.FloatField(verbose_name='Monto ejecutado II semestre',blank=True,null=True)
    insumos = models.CharField(max_length=250,blank=True,null=True)
    actores = models.CharField(max_length=250,blank=True,null=True)
    responsable = models.CharField(max_length=250,blank=True,null=True)
    meses = MultiSelectField(choices=MESES_CHOICES,verbose_name='Meses planificado')
    meses_ejecucion = MultiSelectField(choices=MESES_CHOICES,blank=True,null=True)
    avance_semestre_1 = models.TextField(blank=True,null=True,verbose_name='Avance I semestre')
    avance_semestre_2 = models.TextField(blank=True,null=True,verbose_name='Avance II semestre')

    class Meta:
        verbose_name_plural = 'Sub Actividades'
        verbose_name = 'Sub Actividad'

class Funcionamiento(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Funcionamiento'
        verbose_name = 'Funcionamiento'

class InlineCostoAdmin(models.Model):
    funcionamiento = models.ForeignKey(Funcionamiento, on_delete=models.CASCADE)
    costo_admin = models.ForeignKey(CostoAdministrativo, on_delete=models.CASCADE)
    monto_presupuestado = models.FloatField()
    monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado al I semestre',blank=True,null=True)
    monto_final_anio = models.FloatField(verbose_name='Monto ejecutado al final del año',blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Costo administrativo'
        verbose_name = 'Costo administrativo'

class InlineSalarioProgramatico(models.Model):
    funcionamiento = models.ForeignKey(Funcionamiento, on_delete=models.CASCADE)
    salario_programatico = models.ForeignKey(SalarioProgramatico, on_delete=models.CASCADE)
    monto_presupuestado = models.FloatField()
    monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado al I semestre',blank=True,null=True)
    monto_final_anio = models.FloatField(verbose_name='Monto ejecutado al final del año',blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Salario Programatico'
        verbose_name = 'Salario Programatico'
