from django.shortcuts import render
from .models import *

# Create your views here.
def index(request,template='index.html'):
	proyecto =  Proyecto.objects.first()
	objetivos = Objetivo.objects.filter(proyecto = proyecto)
	efectos = Efecto.objects.filter(proyecto = proyecto)
	productos = Producto.objects.filter(proyecto = proyecto)
	
	return render(request, template, locals())

#export table
def save_as_xls(request):
    tabla = request.POST['tabla']  
    response = render(request,'xls.html', {'tabla': tabla, })
    response['Content-Disposition'] = 'attachment; filename=tabla.xls'
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset'] ='UTF-8'
    return response