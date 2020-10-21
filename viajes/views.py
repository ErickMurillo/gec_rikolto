from django.shortcuts import render
from .models import *
import collections
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def viajes(request,id=None,template='viajes/viaje.html'):
    proyecto = Proyecto.objects.get(id = id)
    anios = Viajes.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anios:
        viaje = InlineViaje.objects.filter(viaje__proyecto = proyecto,viaje__anio = anio)
        dict_anios[anio] = viaje

    return render(request, template, locals())
