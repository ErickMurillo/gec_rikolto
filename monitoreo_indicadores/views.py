from django.shortcuts import render
from .models import *
from modulo_gerencia.models import *
import json as simplejson
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def indicadores_objetivo(request,id=None,template='indicadores/objetivo.html'):
	proyecto = Proyecto.objects.get(id = id)
	object = IndObjetivos.objects.filter(proyecto = id)
	return render(request, template, locals())

@login_required
def indicadores_efectos(request,id=None,template='indicadores/efecto.html'):
	proyecto = Proyecto.objects.get(id = id)
	object = IndEfectos.objects.filter(proyecto = id).order_by('efecto')
	return render(request, template, locals())

@login_required
def indicadores_productos(request,id=None,template='indicadores/producto.html'):
	proyecto = Proyecto.objects.get(id = id)
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