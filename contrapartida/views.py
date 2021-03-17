from django.shortcuts import render
from .models import *
from poa.models import *
from django.contrib.auth.decorators import login_required
import collections
from django.db.models.functions import Coalesce
from django.db.models import Sum, F

# Create your views here.
@login_required
def contrapartida(request,id=None,template='contrapartida/contrapartida.html'):
    proyecto = Proyecto.objects.get(id = id)
    years = []
    for anio in Funcionamiento.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct():
        years.append(anio)

    for anio in Contrapartida.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct():
        years.append(anio)

    dict_anios = collections.OrderedDict()
    for anio in list(sorted(set(years))):
        contrapartida = Contrapartida.objects.filter(proyecto = id,anio = anio)

        lista = []
        dict_anios[anio] = lista
        funcionamiento_costo = InlineCostoAdmin.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
        #funcionamiento general
        fun_general = funcionamiento_costo.exclude(costo_admin__nombre = 'Overhead').aggregate(total = Coalesce(Sum('total'),0.0))['total']
        costo_admin = fun_general

        salario_programatico = InlineSalarioProgramatico.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
        sum_sub_act = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio).aggregate(total_suma = Coalesce(Sum('total'),0.0))['total_suma']
        suma_salario = salario_programatico.aggregate(total = Coalesce(Sum('total'),0.0))['total']
        funcionamiento_programatico = suma_salario + sum_sub_act

        efectos = Poa.objects.filter(proyecto = id,anio = anio).aggregate(total = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0))['total']

        total_gastos = fun_general + funcionamiento_programatico

        overhead = funcionamiento_costo.filter(costo_admin__nombre = 'Overhead').aggregate(total = Coalesce(Sum('total'),0.0))['total']
        total_general = total_gastos + overhead

        lista.append((proyecto.financiadores.all(),fun_general,costo_admin,funcionamiento_programatico,suma_salario,efectos,total_gastos,overhead,total_general))

        id_org = InlineContrapartida.objects.filter(contrapartida__proyecto = id,contrapartida__anio = anio).values_list('organizacion',flat=True).distinct()
        organizaciones = OrgImplementador.objects.filter(id__in = id_org)

        #columna totales
        fun_general_total = 0
        costo_admin_total = 0
        fg_programatico_total = 0
        salario_programatico_total = 0
        efectos_total = 0
        total_gastos_total = 0
        overhead_total = 0
        total_general_total = 0
        total_total = 0
        ##########
        for org in organizaciones:
            contrapartida = InlineContrapartida.objects.filter(contrapartida__proyecto = id,contrapartida__anio = anio,organizacion = org)
            fun_general_contra = contrapartida.aggregate(total = Coalesce(Sum('costos_admin'),0.0))['total']
            costo_admin_contra = fun_general_contra

            salario_programatico_contra = contrapartida.aggregate(total = Coalesce(Sum('salario_programatico'),0.0))['total']
            efectos_contra = contrapartida.aggregate(total = Coalesce(Sum('aporte_actividades'),0.0))['total']

            funcionamiento_programatico_contra = salario_programatico_contra + efectos_contra

            total_gastos_contra = fun_general_contra + funcionamiento_programatico_contra

            overhead_contra = contrapartida.aggregate(total = Coalesce(Sum('overhead'),0.0))['total']

            total_general_contra = total_gastos_contra + overhead_contra

            lista.append((org,fun_general_contra,costo_admin_contra,funcionamiento_programatico_contra,salario_programatico_contra,
                            efectos_contra,total_gastos_contra,overhead_contra,total_general_contra))

            fun_general_total += fun_general_contra
            costo_admin_total += costo_admin_contra
            fg_programatico_total += funcionamiento_programatico_contra
            salario_programatico_total += salario_programatico_contra
            efectos_total += efectos_contra
            total_gastos_total += total_gastos_contra
            overhead_total += overhead_contra
            total_general_total += total_general_contra
            total_total += total_general_contra

        #total
        fun_general_total += fun_general
        costo_admin_total += costo_admin
        fg_programatico_total += funcionamiento_programatico
        salario_programatico_total += suma_salario
        efectos_total += efectos
        total_gastos_total += total_gastos
        overhead_total += overhead
        total_general_total += total_general
        lista.append(('Total',fun_general_total,costo_admin_total,fg_programatico_total,salario_programatico_total,efectos_total,
                        total_gastos_total,overhead_total,total_general_total))

        total_total += total_general

    return render(request, template, locals())
