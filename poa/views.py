from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,F
import collections
from django.db.models.functions import Coalesce
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
                    sum_sub_act_presupuesto = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_semestre_1'))['total_suma']
                    dict_actividad[act,sum_sub_act,sum_sub_act_presupuesto] = sub_actividades

    return render(request, template, locals())

@login_required
def informe_poa_anual(request,id=None,template='poa/informe_anual.html'):
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
                    sum_sub_act_presupuesto = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_final_anio'))['total_suma']
                    dict_actividad[act,sum_sub_act,sum_sub_act_presupuesto] = sub_actividades

    return render(request, template, locals())

@login_required
def ejecucion_financiera(request,id=None,template='poa/ejecucion_financiera.html'):
    proyecto = Proyecto.objects.get(id = id)
    years = []
    for anio in Funcionamiento.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct():
        years.append(anio)

    for anio in Poa.objects.filter(proyecto = id).order_by('anio').values_list('anio',flat=True).distinct():
        years.append(anio)

    dict_anios = collections.OrderedDict()
    for anio in list(sorted(set(years))):
        dict = collections.OrderedDict()
        dict_anios[anio] = dict
        funcionamiento_costo = InlineCostoAdmin.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
        #funcionamiento general
        fun_general = funcionamiento_costo.aggregate(total = Coalesce(Sum('monto_presupuestado'),0.0))['total']
        dict['Funcionamiento General'] = fun_general

        #costo administrativo
        costo_admin = funcionamiento_costo.aggregate(presupuesto = Sum('monto_presupuestado'),
                                    semestre_1 = Sum('monto_semestre_1'),
                                    final_anio = Sum('monto_final_anio'),
                                    acumulado = Sum(F('monto_semestre_1') + F('monto_final_anio')))

        dict['Costos Administrativos'] = (costo_admin['presupuesto'],
                                         costo_admin['semestre_1'],
                                         costo_admin['final_anio'],
                                         costo_admin['acumulado'],
                                         saca_porcentajes(costo_admin['acumulado'],costo_admin['presupuesto'],False))

        #detalle costo admin
        id_costo_admin = funcionamiento_costo.values_list('costo_admin',flat=True).distinct()
        nombre_costo_admin = CostoAdministrativo.objects.filter(id__in = id_costo_admin)
        for obj in nombre_costo_admin:
            costo_admin_detalle = funcionamiento_costo.filter(costo_admin = obj).aggregate(presupuesto = Sum('monto_presupuestado'),
                                        semestre_1 = Sum('monto_semestre_1'),
                                        final_anio = Sum('monto_final_anio'),
                                        acumulado = Sum(F('monto_semestre_1') + F('monto_final_anio')))

            dict[obj] = (costo_admin_detalle['presupuesto'],
                         costo_admin_detalle['semestre_1'],
                         costo_admin_detalle['final_anio'],
                         costo_admin_detalle['acumulado'],
                         saca_porcentajes(costo_admin_detalle['acumulado'],costo_admin_detalle['presupuesto'],False))

        #funcionamiento programatico
        salario_programatico = InlineSalarioProgramatico.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
        sum_sub_act = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio).aggregate(total_suma = Coalesce(Sum('monto_presupuestado'),0.0))['total_suma']
        suma_salario = salario_programatico.aggregate(total = Coalesce(Sum('monto_presupuestado'),0.0))['total']
        funcionamiento_programatico = suma_salario + sum_sub_act
        dict['Funcionamiento Programático'] = funcionamiento_programatico

        #salario programatico
        salario = salario_programatico.aggregate(presupuesto = Sum('monto_presupuestado'),
                                    semestre_1 = Sum('monto_semestre_1'),
                                    final_anio = Sum('monto_final_anio'),
                                    acumulado = Sum(F('monto_semestre_1') + F('monto_final_anio')))

        dict['Salario Programático'] = (salario['presupuesto'],
                                         salario['semestre_1'],
                                         salario['final_anio'],
                                         salario['acumulado'],
                                         saca_porcentajes(salario['acumulado'],salario['presupuesto'],False))

        #detalle salario programatico
        id_salario = salario_programatico.values_list('salario_programatico',flat=True).distinct()
        nombre_salario = SalarioProgramatico.objects.filter(id__in = id_salario)
        for obj in nombre_salario:
            salario_detalle = salario_programatico.filter(salario_programatico = obj).aggregate(presupuesto = Sum('monto_presupuestado'),
                                        semestre_1 = Sum('monto_semestre_1'),
                                        final_anio = Sum('monto_final_anio'),
                                        acumulado = Sum(F('monto_semestre_1') + F('monto_final_anio')))

            dict[obj] = (salario_detalle['presupuesto'],
                         salario_detalle['semestre_1'],
                         salario_detalle['final_anio'],
                         salario_detalle['acumulado'],
                         saca_porcentajes(salario_detalle['acumulado'],salario_detalle['presupuesto'],False))


        #actividades de programa
        dict['ACTIVIDADES DEL PROGRAMA'] = sum_sub_act

        #Efectos
        poa_efectos = Poa.objects.filter(proyecto = id,anio = anio).values_list('actividadespoa__actividad__producto__efecto',flat=True).distinct()
        efectos = Efecto.objects.filter(id__in = poa_efectos)

        for obj in efectos:
            efectos_query = Poa.objects.filter(proyecto = id,anio = anio,
                            actividadespoa__actividad__producto__efecto = obj)
            list_prods = efectos_query.values_list('actividadespoa__actividad__producto',flat=True).distinct()
            nombre_efecto = "Efecto " + str(obj)
            dict[nombre_efecto] = efectos_query.aggregate(total = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0))['total']

            #productos
            productos = Producto.objects.filter(id__in = list_prods)
            for prod in productos:
                productos_query = Poa.objects.filter(proyecto = id,anio = anio,
                                actividadespoa__actividad__producto = prod,
                                actividadespoa__actividad__producto__efecto = obj
                                )
                list_act = productos_query.values_list('actividadespoa__actividad',flat=True).distinct()
                nombre_producto = "Producto " + str(prod)
                dict[nombre_producto] = productos_query.aggregate(total = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0))['total']

                #actividades
                actividades = Actividades.objects.filter(id__in = list_act)
                for act in actividades:
                    actividades_query = Poa.objects.filter(proyecto = id,anio = anio,
                                    actividadespoa__actividad = act,
                                    actividadespoa__actividad__producto = prod,
                                    actividadespoa__actividad__producto__efecto = obj)
                    nombre_actividad = "Actividad " + str(act)
                    dict[nombre_actividad] = actividades_query.aggregate(total = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0))['total']
                    sub_activdades = sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
                    for sub in sub_activdades:
                        nombre_sub_actividad = str(sub.identificador) + " - " + str(sub.descripcion)
                        dict[nombre_sub_actividad] = sub.monto_presupuestado
        dict['TOTAL GENERAL'] = fun_general + funcionamiento_programatico
        # print(dict_anios)
    return render(request, template, locals())

def saca_porcentajes(dato, total, formato=True):
	if dato != None:
		try:
			porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
		except:
			return 0
		if formato:
			return porcentaje
		else:
			return '%.2f' % porcentaje
	else:
		return 0
