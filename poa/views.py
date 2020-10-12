from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
# Create your views here.

def poa(request,id=None,template='poa.html'):
    proyecto = Proyecto.objects.get(id = id)
    anio_poa = Poa.objects.filter(proyecto = id).values_list('anio',flat=True).distinct()

    if request.GET.get('anio'):
        anio = request.GET['anio']
        poa = Poa.objects.filter(proyecto = id,anio = anio)

        poa_efectos = IndicadoresPOA.objects.filter(poa__proyecto = id,poa__anio = anio).values_list('indicador__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)
        dict_poa = {}
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