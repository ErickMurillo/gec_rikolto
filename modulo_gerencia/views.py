from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
import collections
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request,template='index.html'):
	proyectos = Proyecto.objects.order_by('nombre')
	return render(request, template, locals())

@login_required
def marco_logico(request,id,template='marco_logico/marco_logico.html'):
	proyecto =  Proyecto.objects.get(id = id)
	objetivos = Objetivo.objects.filter(proyecto = proyecto)
	efectos = Efecto.objects.filter(proyecto = proyecto)
	productos = Producto.objects.filter(proyecto = proyecto)
	dict = collections.OrderedDict()
	for obj in productos:
		actividad = Actividades.objects.filter(producto = obj).order_by('identificador')
		dict[obj,actividad.count()] = actividad
	return render(request, template, locals())

#export table
def save_as_xls(request):
	tabla = request.POST['tabla']
	response = render(request,'xls.html', {'tabla': tabla, })
	response['Content-Disposition'] = 'attachment; filename=tabla.xls'
	response['Content-Type'] = 'application/vnd.ms-excel'
	response['Charset'] ='UTF-8'
	return response
