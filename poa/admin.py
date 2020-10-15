from django.contrib import admin
from .models import *

# Register your models here.

class IndicadoresPOA_Inline(admin.TabularInline):
	model = IndicadoresPOA
	extra = 1
	
class PoaAdmin(admin.ModelAdmin):
	inlines = [IndicadoresPOA_Inline]
	autocomplete_fields = ['actividad']
	list_display = ('anio', 'actividad')

admin.site.register(Poa,PoaAdmin)
