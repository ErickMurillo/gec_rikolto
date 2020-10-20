from django.shortcuts import render
from .models import *
import collections
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def plan_proyectos(request,id=None,template='proyectos_financiados/plan.html'):
    proyecto = Proyecto.objects.get(id = id)
    anios = ProyectosFinanciados.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anios:
        proyectos = InlineProyecto.objects.filter(proyectos_financiados__proyecto = proyecto,proyectos_financiados__anio = anio)
        dict_anios[anio] = proyectos

    return render(request, template, locals())

@login_required
def informe_proyectos(request,id=None,template='proyectos_financiados/informe.html'):
    proyecto = Proyecto.objects.get(id = id)
    anios = ProyectosFinanciados.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anios:
        proyectos = InlineProyecto.objects.filter(proyectos_financiados__proyecto = proyecto,proyectos_financiados__anio = anio)
        productos = ProductoProyecto.objects.filter(inline_proyecto__proyectos_financiados__proyecto = proyecto,inline_proyecto__proyectos_financiados__anio = anio)
        dict_anios[anio] = proyectos,productos

    return render(request, template, locals())
