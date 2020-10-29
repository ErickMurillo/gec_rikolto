from django.contrib import admin
from .models import *
import nested_admin
from django.forms import TextInput, Textarea, SelectMultiple
from django.db import models
from .forms import *

# Register your models here.

class SubActividadesPOA_Inline(nested_admin.NestedTabularInline):
	model = SubActividadesPOA
	extra = 1
	formfield_overrides = {
		models.CharField: {'widget': Textarea(attrs={'rows': 1,'cols': 18,'style': 'height: 100px;resize:none;',})},
		models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':40,'style': 'height: 100px;resize:none;',})},
	}
	form = SubActividadesPOAAdminForm

	class Media:
		css = {'all':('css/inlines.css',)}


class ActividadesPOA_Inline(nested_admin.NestedTabularInline):
	model = ActividadesPOA
	extra = 1
	inlines = [SubActividadesPOA_Inline,]
	autocomplete_fields = ['actividad']
	form = ActividadesPOAForm

class PoaAdmin(nested_admin.NestedModelAdmin):
	inlines = [ActividadesPOA_Inline]
	# list_display = ('anio', 'actividad')
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Poa.objects.all()
		return Poa.objects.filter(usuario=request.user)

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
		return super(PoaAdmin, self).get_form(request, obj=None, **kwargs)

class InlineCostoAdmin_Inline(admin.TabularInline):
	model = InlineCostoAdmin
	extra = 1

class InlineSalarioProgramatico_Inline(admin.TabularInline):
	model = InlineSalarioProgramatico
	extra = 1

class FuncionamientoAdmin(admin.ModelAdmin):
	inlines = [InlineCostoAdmin_Inline,InlineSalarioProgramatico_Inline]
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Funcionamiento.objects.all()
		return Funcionamiento.objects.filter(usuario=request.user)

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
		return super(FuncionamientoAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(Poa,PoaAdmin)
admin.site.register(Funcionamiento,FuncionamientoAdmin)
