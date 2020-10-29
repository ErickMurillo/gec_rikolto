from django.db import models
from modulo_gerencia.models import *
from listas.models import *
from django.contrib.auth.models import User

# Create your models here.
class Documentos(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    anio = models.IntegerField(verbose_name="Año")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (str(self.anio))

    class Meta:
        verbose_name_plural = 'Documentos'
        verbose_name = 'Documento'

SEMESTRE_CHOICES = (('I','I'),('II','II'))

class InlineDocumentos(models.Model):
    documento = models.ForeignKey(Documentos, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    semestre = models.CharField(max_length=2,choices=SEMESTRE_CHOICES)
    fuente = models.ForeignKey(FuenteDocumentos, on_delete=models.CASCADE)
    url = models.URLField(null=True,blank=True)
    archivo = models.FileField(upload_to='documentos/',null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Documentos'
        verbose_name = 'Documento'
