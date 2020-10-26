from django.shortcuts import render
from .models import *
import collections
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def documentos(request,id,template='documentos/documentos.html'):
    proyecto = Proyecto.objects.get(id = id)
    anios = Documentos.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anios:
        documentos = InlineDocumentos.objects.filter(documento__proyecto = proyecto,documento__anio = anio)
        dict_anios[anio] = documentos

    return render(request, template, locals())
