from django.db import models
from listas.models import *
from modulo_gerencia.models import *

# Create your models here.
class ProyectosFinanciados(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Convenios de Colaboración'
        verbose_name = 'Convenio de Colaboración'

class InlineProyecto(models.Model):
    proyectos_financiados = models.ForeignKey(ProyectosFinanciados, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(ProyectoFinanciado, on_delete=models.CASCADE,verbose_name='Título')
    org_implementadora = models.ForeignKey(OrgImplementador, on_delete=models.CASCADE)
    semestre_1 = models.BooleanField()
    semestre_2 = models.BooleanField()
    paises_influencia = models.ManyToManyField(Pais)
    monto_presupuestado = models.FloatField()
    monto_semestre_1 = models.FloatField(verbose_name='Monto ejecutado al I semestre',blank=True,null=True)
    monto_final_anio = models.FloatField(verbose_name='Monto ejecutado al final del año',blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Convenios'
        verbose_name = 'Convenio'

SEMESTRE_CHOICES = (('I','I'),('II','II'))

class ProductoProyecto(models.Model):
    inline_proyecto = models.ForeignKey(InlineProyecto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    anio = models.IntegerField(verbose_name="Año")
    semestre = models.CharField(max_length=2,choices=SEMESTRE_CHOICES)
    paises_influencia = models.ManyToManyField(Pais)
    url = models.URLField(null=True,blank=True)
    archivo = models.FileField(upload_to='producto-proy-financiados/',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
