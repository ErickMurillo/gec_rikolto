from django.shortcuts import render
from .models import *

# Create your views here.
def indicadores_objetivo(request,id=None,template='indicadores_obj.html'):
	object = IndObjetivos.objects.filter(proyecto = id).order_by('indicador')
	return render(request, template, locals())