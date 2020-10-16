from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import collections
# Create your views here.

@login_required
def plan_poa(request,id=None,template='poa/plan.html'):
    proyecto = Proyecto.objects.get(id = id)
    anio_poa = Poa.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anio_poa:
        poa = Poa.objects.filter(proyecto = id,anio = anio)
        poa_efectos = Poa.objects.filter(proyecto = id,anio = anio).values_list('actividadespoa__actividad__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)
        dict_poa = collections.OrderedDict()
        dict_anios[anio] = dict_poa
        for efecto in efectos:
            poa_productos = Poa.objects.filter(proyecto = id,anio = anio,
                            actividadespoa__actividad__producto__efecto = efecto).values_list('actividadespoa__actividad__producto',flat=True).distinct()
            productos = Producto.objects.filter(id__in = poa_productos)
            dict = collections.OrderedDict()
            dict_poa[efecto] = dict
            
            for obj in productos:
                actividad_poa = Poa.objects.filter(proyecto = id,anio = anio,actividadespoa__actividad__producto = obj).values_list('actividadespoa__actividad',flat=True).distinct()
                actividades = Actividades.objects.filter(id__in = actividad_poa)
                dict_actividad = collections.OrderedDict()
                dict[obj] = dict_actividad

                for act in actividades:
                    sum_sub_act = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_presupuestado'))['total_suma']
                    sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
                    dict_actividad[act,sum_sub_act] = sub_actividades

    return render(request, template, locals())

@login_required
def informe_poa(request,id=None,template='poa/informe.html'):
    proyecto = Proyecto.objects.get(id = id)
    anio_poa = Poa.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct()

    dict_anios = collections.OrderedDict()
    for anio in anio_poa:
        poa = Poa.objects.filter(proyecto = id,anio = anio)
        poa_efectos = Poa.objects.filter(proyecto = id,anio = anio).values_list('actividadespoa__actividad__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)
        dict_poa = collections.OrderedDict()
        dict_anios[anio] = dict_poa
        for efecto in efectos:
            poa_productos = Poa.objects.filter(proyecto = id,anio = anio,
                            actividadespoa__actividad__producto__efecto = efecto).values_list('actividadespoa__actividad__producto',flat=True).distinct()
            productos = Producto.objects.filter(id__in = poa_productos)
            dict = collections.OrderedDict()
            dict_poa[efecto] = dict
            
            for obj in productos:
                actividad_poa = Poa.objects.filter(proyecto = id,anio = anio,actividadespoa__actividad__producto = obj).values_list('actividadespoa__actividad',flat=True).distinct()
                actividades = Actividades.objects.filter(id__in = actividad_poa)
                dict_actividad = collections.OrderedDict()
                dict[obj] = dict_actividad

                for act in actividades:
                    sum_sub_act = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_presupuestado'))['total_suma']
                    sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
                    dict_actividad[act,sum_sub_act] = sub_actividades

    return render(request, template, locals())