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
		models.CharField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 30,
								  'style': 'height: 100px;resize:none;',})},
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

class InlineCostoAdmin_Inline(admin.TabularInline):
	model = InlineCostoAdmin
	extra = 1

class InlineSalarioProgramatico_Inline(admin.TabularInline):
	model = InlineSalarioProgramatico
	extra = 1

class FuncionamientoAdmin(admin.ModelAdmin):
	inlines = [InlineCostoAdmin_Inline,InlineSalarioProgramatico_Inline]

admin.site.register(Poa,PoaAdmin)
admin.site.register(Funcionamiento,FuncionamientoAdmin)
