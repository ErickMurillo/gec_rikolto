from django.contrib import admin
from .models import *
import nested_admin

# Register your models here.
class ProductoProyecto_Inline(nested_admin.NestedTabularInline):
	model = ProductoProyecto
	extra = 1

class InlineProyecto_Inline(nested_admin.NestedTabularInline):
	model = InlineProyecto
	extra = 1
	inlines = [ProductoProyecto_Inline,]

class ProyectosFinanciadosAdmin(nested_admin.NestedModelAdmin):
	inlines = [InlineProyecto_Inline,]
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return ProyectosFinanciados.objects.all()
		return ProyectosFinanciados.objects.filter(usuario=request.user)

	def save_model(self, request, obj, form, change):
		if request.user.is_superuser:
			obj.save()
		else:
			obj.usuario = request.user
			obj.save()

	def get_form(self, request, obj=None, **kwargs):
		if not request.user.is_superuser:
			self.exclude = ('usuario',)
		else:
			self.exclude = ()
		return super(ProyectosFinanciadosAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(ProyectosFinanciados,ProyectosFinanciadosAdmin)
