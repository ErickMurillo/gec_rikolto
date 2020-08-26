from django.contrib import admin
from .models import *

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
	filter_horizontal = ['financiadores','aliados',]

class IndicadoresObjetivos_Inline(admin.TabularInline):
	model = IndicadoresObjetivos
	extra = 1

class ObjetivoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresObjetivos_Inline,]

class IndicadoresEfectos_Inline(admin.TabularInline):
	model = IndicadoresEfectos
	extra = 1

class EfectoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresEfectos_Inline,]

class IndicadoresProductos_Inline(admin.TabularInline):
	model = IndicadoresProductos
	extra = 1

class ProductoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresProductos_Inline,]

class ObjInd1_Inline(admin.TabularInline):
	model = ObjInd1
	extra = 1

class ObjInd2_Inline(admin.TabularInline):
	model = ObjInd2
	extra = 1

class ObjInd3_Inline(admin.TabularInline):
	model = ObjInd3
	extra = 1

class ObjInd4_Inline(admin.TabularInline):
	model = ObjInd4
	extra = 1

class IndObjetivosAdmin(admin.ModelAdmin):
	inlines = [ObjInd1_Inline,ObjInd2_Inline,ObjInd3_Inline,ObjInd4_Inline,]
	
	class Media:
		js = ('js/admin.js',)

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Objetivo,ObjetivoAdmin)
admin.site.register(Efecto,EfectoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Actividades)
admin.site.register(IndObjetivos,IndObjetivosAdmin)
