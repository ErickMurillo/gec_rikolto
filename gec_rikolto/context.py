from modulo_gerencia.models import *

def globales(request):
	id_proyecto = Proyecto.objects.values_list('id',flat=True).first()

	return {'id':id_proyecto,}