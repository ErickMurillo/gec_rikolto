from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
# Create your views here.

def plan_poa(request,id=None,template='poa/plan.html'):
    proyecto = Proyecto.objects.get(id = id)
    anio_poa = Poa.objects.filter(proyecto = id).values_list('anio',flat=True).distinct()

    dict_anios = {}
    for anio in anio_poa:
        poa = Poa.objects.filter(proyecto = id,anio = anio)
        poa_efectos = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio).values_list('indicador__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)
        dict_poa = {}
        dict_anios[anio] = dict_poa
        for efecto in efectos:
            poa_productos = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio,
                            indicador__producto__efecto = efecto).values_list('indicador__producto',flat=True).distinct()
            productos = Producto.objects.filter(id__in = poa_productos)
            dict = {}
            dict_poa[efecto] = dict
            
            for obj in productos:
                actividad = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio,indicador__producto = obj)
                dict[obj] = actividad

    return render(request, template, locals())

def informe_poa(request,id=None,template='poa/informe.html'):
    proyecto = Proyecto.objects.get(id = id)
    anio_poa = Poa.objects.filter(proyecto = id).values_list('anio',flat=True).distinct()

    dict_anios = {}
    for anio in anio_poa:
        poa = Poa.objects.filter(proyecto = id,anio = anio)
        poa_efectos = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio).values_list('indicador__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)
        dict_poa = {}
        dict_anios[anio] = dict_poa
        for efecto in efectos:
            poa_productos = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio,
                            indicador__producto__efecto = efecto).values_list('indicador__producto',flat=True).distinct()
            productos = Producto.objects.filter(id__in = poa_productos)
            dict = {}
            dict_poa[efecto] = dict
            
            for obj in productos:
                actividad = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio,indicador__producto = obj)
                dict[obj] = actividad

    return render(request, template, locals())