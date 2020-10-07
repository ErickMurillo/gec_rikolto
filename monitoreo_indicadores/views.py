from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
import json as simplejson
from django.http import HttpResponse

# Create your views here.
def indicadores_objetivo(request,id=None,template='indicadores/objetivo.html'):
	proyecto = Proyecto.objects.get(id = id)
	objetivos = IndObjetivos.objects.filter(proyecto = id).values_list('objetivo__identificador','objetivo__descripcion','objetivo').distinct('objetivo')
	dict = {}
	for obj in objetivos:
		indicadores = IndObjetivos.objects.filter(objetivo=obj[2])
		dict[obj] = indicadores

	return render(request, template, locals())

def indicadores_efectos(request,id=None,template='indicadores/efecto.html'):
	proyecto = Proyecto.objects.get(id = id)
	efectos = IndEfectos.objects.filter(proyecto = id).values_list('efecto__identificador','efecto__descripcion','efecto').distinct('efecto')
	dict = {}
	for obj in efectos:
		indicadores = IndEfectos.objects.filter(efecto=obj[2])
		dict[obj] = indicadores

	return render(request, template, locals())

def indicadores_productos(request,id=None,template='indicadores/producto.html'):
	proyecto = Proyecto.objects.get(id = id)
	productos = IndProductos.objects.filter(proyecto = id).values_list('producto__identificador','producto__descripcion','producto').distinct('producto')
	dict = {}
	for obj in productos:
		indicadores = IndProductos.objects.filter(producto=obj[2])
		dict[obj] = indicadores
	return render(request, template, locals())

#ajax
def producto_admin(request):
	id = request.GET.get('id', '')
	indicador = IndicadoresProductos.objects.get(id = id)
	lista = [indicador.identificador]
	return HttpResponse(simplejson.dumps(lista), content_type = 'application/json')

def efecto_admin(request):
	id = request.GET.get('id', '')
	indicador = IndicadoresEfectos.objects.get(id = id)
	lista = [indicador.identificador]
	return HttpResponse(simplejson.dumps(lista), content_type = 'application/json')