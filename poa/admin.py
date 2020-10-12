from django.contrib import admin
from .models import *

# Register your models here.

class IndicadoresPOA_Inline(admin.TabularInline):
	model = IndicadoresPOA
	extra = 1
	autocomplete_fields = ['indicador']

class PoaAdmin(admin.ModelAdmin):
	inlines = [IndicadoresPOA_Inline]

admin.site.register(Poa,PoaAdmin)
