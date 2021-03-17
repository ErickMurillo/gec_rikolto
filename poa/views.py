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
					sum_sub_act_modificado = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('total'))['total_suma']
					sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
					dict_actividad[act,sum_sub_act,sum_sub_act_modificado] = sub_actividades

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
					sum_sub_act_ajuste = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('ajuste'))['total_suma']
					presupuesto_modificado = sum_sub_act + sum_sub_act_ajuste
					sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
					sum_sub_act_presupuesto = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_semestre_1'))['total_suma']
					dict_actividad[act,sum_sub_act,sum_sub_act_presupuesto,presupuesto_modificado] = sub_actividades

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
					sum_sub_act_ajuste = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('ajuste'))['total_suma']
					presupuesto_modificado = sum_sub_act + sum_sub_act_ajuste
					sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
					sum_sub_act_presupuesto = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act).aggregate(total_suma = Sum('monto_final_anio'))['total_suma']
					dict_actividad[act,sum_sub_act,sum_sub_act_presupuesto,presupuesto_modificado] = sub_actividades

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
		total_semestre_1 = 0
		total_semestre_2 = 0
		acumulado_total = 0
		total_modificado = 0

		dict = collections.OrderedDict()
		dict_anios[anio] = dict
		funcionamiento_costo = InlineCostoAdmin.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
		#funcionamiento general
		fun_general = funcionamiento_costo.aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
									modificado = Coalesce(Sum('total'),0.0),
									semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
									final_anio = Coalesce(Sum('monto_final_anio'),0.0),
									acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))
		dict['Funcionamiento General'] = (fun_general['presupuesto'],
											fun_general['modificado'],
											fun_general['semestre_1'],
											fun_general['final_anio'],
											fun_general['acumulado'],
											saca_porcentajes(fun_general['acumulado'],fun_general['modificado'],False))

		total_semestre_1 += fun_general['semestre_1']
		total_semestre_2 += fun_general['final_anio']
		acumulado_total += fun_general['acumulado']
		total_modificado += fun_general['modificado']
		#costo administrativo
		costo_admin = funcionamiento_costo.aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
									modificado = Coalesce(Sum('total'),0.0),
									semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
									final_anio = Coalesce(Sum('monto_final_anio'),0.0),
									acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

		dict['Costos Administrativos'] = (costo_admin['presupuesto'],
										 costo_admin['modificado'],
										 costo_admin['semestre_1'],
										 costo_admin['final_anio'],
										 costo_admin['acumulado'],
										 saca_porcentajes(costo_admin['acumulado'],costo_admin['modificado'],False))

		#detalle costo admin
		id_costo_admin = funcionamiento_costo.values_list('costo_admin',flat=True).distinct()
		nombre_costo_admin = CostoAdministrativo.objects.filter(id__in = id_costo_admin)
		for obj in nombre_costo_admin:
			costo_admin_detalle = funcionamiento_costo.filter(costo_admin = obj).aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
										modificado = Coalesce(Sum('total'),0.0),
										semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
										final_anio = Coalesce(Sum('monto_final_anio'),0.0),
										acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

			dict[obj] = (costo_admin_detalle['presupuesto'],
						 costo_admin_detalle['modificado'],
						 costo_admin_detalle['semestre_1'],
						 costo_admin_detalle['final_anio'],
						 costo_admin_detalle['acumulado'],
						 saca_porcentajes(costo_admin_detalle['acumulado'],costo_admin_detalle['modificado'],False))

		#funcionamiento programatico
		salario_programatico = InlineSalarioProgramatico.objects.filter(funcionamiento__proyecto = id, funcionamiento__anio = anio)
		sum_sub_act = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio).aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
														modificado = Coalesce(Sum('total'),0.0),
														semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
														final_anio = Coalesce(Sum('monto_final_anio'),0.0),
														acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

		suma_salario = salario_programatico.aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
														modificado = Coalesce(Sum('total'),0.0),
														semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
														final_anio = Coalesce(Sum('monto_final_anio'),0.0),
														acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))
		funcionamiento_programatico = suma_salario['presupuesto'] + sum_sub_act['presupuesto']
		funcionamiento_programatico_modificado = suma_salario['modificado'] + sum_sub_act['modificado']

		acumulado_programatico = suma_salario['acumulado'] + sum_sub_act['acumulado']
		dict['Funcionamiento Programático'] = (funcionamiento_programatico,
												funcionamiento_programatico_modificado,
												suma_salario['semestre_1'] + sum_sub_act['semestre_1'],
												suma_salario['final_anio'] + sum_sub_act['final_anio'],
												acumulado_programatico,
												saca_porcentajes(acumulado_programatico,funcionamiento_programatico_modificado,False))

		total_semestre_1 += suma_salario['semestre_1']
		total_semestre_2 += suma_salario['final_anio']
		acumulado_total += suma_salario['acumulado']
		total_modificado += suma_salario['modificado']
		#salario programatico
		salario = salario_programatico.aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
									modificado = Coalesce(Sum('total'),0.0),
									semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
									final_anio = Coalesce(Sum('monto_final_anio'),0.0),
									acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

		dict['Salario Programático'] = (salario['presupuesto'],
										 salario['modificado'],
										 salario['semestre_1'],
										 salario['final_anio'],
										 salario['acumulado'],
										 saca_porcentajes(salario['acumulado'],salario['presupuesto'],False))

		#detalle salario programatico
		id_salario = salario_programatico.values_list('salario_programatico',flat=True).distinct()
		nombre_salario = SalarioProgramatico.objects.filter(id__in = id_salario)
		for obj in nombre_salario:
			salario_detalle = salario_programatico.filter(salario_programatico = obj).aggregate(presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
										modificado = Coalesce(Sum('total'),0.0),
										semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
										final_anio = Coalesce(Sum('monto_final_anio'),0.0),
										acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

			dict[obj] = (salario_detalle['presupuesto'],
						 salario_detalle['modificado'],
						 salario_detalle['semestre_1'],
						 salario_detalle['final_anio'],
						 salario_detalle['acumulado'],
						 saca_porcentajes(salario_detalle['acumulado'],salario_detalle['modificado'],False))


		#actividades de programa
		actividades_programa = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio).aggregate(
														presupuesto = Coalesce(Sum('monto_presupuestado'),0.0),
														modificado = Coalesce(Sum('total'),0.0),
														semestre_1 = Coalesce(Sum('monto_semestre_1'),0.0),
														final_anio = Coalesce(Sum('monto_final_anio'),0.0),
														acumulado = Sum(Coalesce(F('monto_semestre_1'),0.0) + Coalesce(F('monto_final_anio'),0.0)))

		dict['ACTIVIDADES DEL PROGRAMA'] = (actividades_programa['presupuesto'],
											 actividades_programa['modificado'],
											 actividades_programa['semestre_1'],
											 actividades_programa['final_anio'],
											 actividades_programa['acumulado'],
											 saca_porcentajes(actividades_programa['acumulado'],actividades_programa['modificado'],False))

		total_semestre_1 += actividades_programa['semestre_1']
		total_semestre_2 += actividades_programa['final_anio']
		acumulado_total += actividades_programa['acumulado']
		total_modificado +=  actividades_programa['modificado']
		#Efectos
		poa_efectos = Poa.objects.filter(proyecto = id,anio = anio).values_list('actividadespoa__actividad__producto__efecto',flat=True).distinct()
		efectos = Efecto.objects.filter(id__in = poa_efectos)

		for obj in efectos:
			efectos_query = Poa.objects.filter(proyecto = id,anio = anio,
							actividadespoa__actividad__producto__efecto = obj)
			list_prods = efectos_query.values_list('actividadespoa__actividad__producto',flat=True).distinct()
			nombre_efecto = "Efecto " + str(obj)
			valores_efecto = efectos_query.aggregate(
											presupuesto = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0),
											modificado = Coalesce(Sum('actividadespoa__subactividadespoa__total'),0.0),
											semestre_1 = Coalesce(Sum('actividadespoa__subactividadespoa__monto_semestre_1'),0.0),
											final_anio = Coalesce(Sum('actividadespoa__subactividadespoa__monto_final_anio'),0.0),
											acumulado = Sum(Coalesce(F('actividadespoa__subactividadespoa__monto_semestre_1'),0.0) + Coalesce(F('actividadespoa__subactividadespoa__monto_final_anio'),0.0)))

			dict[nombre_efecto] = (valores_efecto['presupuesto'],
												 valores_efecto['modificado'],
												 valores_efecto['semestre_1'],
												 valores_efecto['final_anio'],
												 valores_efecto['acumulado'],
												 saca_porcentajes(valores_efecto['acumulado'],valores_efecto['modificado'],False))

			#productos
			productos = Producto.objects.filter(id__in = list_prods)
			for prod in productos:
				productos_query = Poa.objects.filter(proyecto = id,anio = anio,
								actividadespoa__actividad__producto = prod,
								actividadespoa__actividad__producto__efecto = obj
								)
				list_act = productos_query.values_list('actividadespoa__actividad',flat=True).distinct()
				nombre_producto = "Producto " + str(prod)
				valores_producto = productos_query.aggregate(
												presupuesto = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0),
												modificado = Coalesce(Sum('actividadespoa__subactividadespoa__total'),0.0),
												semestre_1 = Coalesce(Sum('actividadespoa__subactividadespoa__monto_semestre_1'),0.0),
												final_anio = Coalesce(Sum('actividadespoa__subactividadespoa__monto_final_anio'),0.0),
												acumulado = Sum(Coalesce(F('actividadespoa__subactividadespoa__monto_semestre_1'),0.0) + Coalesce(F('actividadespoa__subactividadespoa__monto_final_anio'),0.0)))

				dict[nombre_producto] = (valores_producto['presupuesto'],
										valores_producto['modificado'],
										valores_producto['semestre_1'],
										valores_producto['final_anio'],
										valores_producto['acumulado'],
										saca_porcentajes(valores_producto['acumulado'],valores_producto['modificado'],False))


				#actividades
				actividades = Actividades.objects.filter(id__in = list_act)
				for act in actividades:
					actividades_query = Poa.objects.filter(proyecto = id,anio = anio,
									actividadespoa__actividad = act,
									actividadespoa__actividad__producto = prod,
									actividadespoa__actividad__producto__efecto = obj)
					nombre_actividad = "Actividad " + str(act)
					valores_actividad = actividades_query.aggregate(
													presupuesto = Coalesce(Sum('actividadespoa__subactividadespoa__monto_presupuestado'),0.0),
													modificado = Coalesce(Sum('actividadespoa__subactividadespoa__total'),0.0),
													semestre_1 = Coalesce(Sum('actividadespoa__subactividadespoa__monto_semestre_1'),0.0),
													final_anio = Coalesce(Sum('actividadespoa__subactividadespoa__monto_final_anio'),0.0),
													acumulado = Sum(Coalesce(F('actividadespoa__subactividadespoa__monto_semestre_1'),0.0) + Coalesce(F('actividadespoa__subactividadespoa__monto_final_anio'),0.0)))

					dict[nombre_actividad] = (valores_actividad['presupuesto'],
											valores_actividad['modificado'],
											valores_actividad['semestre_1'],
											valores_actividad['final_anio'],
											valores_actividad['acumulado'],
											saca_porcentajes(valores_actividad['acumulado'],valores_actividad['modificado'],False))

					sub_actividades = SubActividadesPOA.objects.filter(actividad_poa__poa__proyecto = id,actividad_poa__poa__anio = anio,actividad_poa__actividad = act)
					for sub in sub_actividades:
						nombre_sub_actividad = str(sub.identificador) + " - " + str(sub.descripcion)
						#validaciones
						if sub.monto_semestre_1:
							monto_semestre_1 = sub.monto_semestre_1
						else:
							monto_semestre_1 = 0.0

						if sub.monto_final_anio:
							monto_final_anio = sub.monto_final_anio
						else:
							monto_final_anio = 0.0

						acumulado = monto_semestre_1 + monto_final_anio
						###############
						dict[nombre_sub_actividad] = (sub.monto_presupuestado,
														sub.total,
														monto_semestre_1,
														monto_final_anio,
														acumulado,
														saca_porcentajes(acumulado,sub.total,False))
		total = fun_general['presupuesto'] + funcionamiento_programatico
		# porcentaje_general = saca_porcentajes(acumulado_total,total,False)
		porcentaje_general = saca_porcentajes(acumulado_total,total_modificado,False)
		dict['TOTAL GENERAL'] = (total,total_modificado,total_semestre_1,total_semestre_2,acumulado_total,porcentaje_general)

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
