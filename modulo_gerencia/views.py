from django.shortcuts import render
from .models import *

# Create your views here.
def index(request,template='index.html'):
	proyecto = Proyecto.objects.all()
	objetivos = Objetivo.objects.all()
	efectos = Efecto.objects.all()
	return render(request, template, locals())


def indicadores_objetivo(request,id=None,template='indicadores_obj.html'):
	object = IndObjetivos.objects.filter(proyecto = id)
	return render(request, template, locals())