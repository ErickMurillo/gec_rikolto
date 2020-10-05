from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
import json as simplejson
from django.http import HttpResponse

# Create your views here.
def indicadores_objetivo(request,id=None,template='indicadores/objetivo.html'):
	object = IndObjetivos.objects.filter(proyecto = id).order_by('indicador')
	return render(request, template, locals())

def indicadores_efectos(request,id=None,template='indicadores/efecto.html'):
	object = IndEfectos.objects.filter(proyecto = id).order_by('indicador')
	return render(request, template, locals())

def indicadores_productos(request,id=None,template='indicadores/producto.html'):
	object = IndProductos.objects.filter(proyecto = id).order_by('indicador')
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