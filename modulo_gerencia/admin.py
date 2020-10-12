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

class ActividadesAdmin(admin.ModelAdmin):
	search_fields = ['identificador','descripcion']

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Objetivo,ObjetivoAdmin)
admin.site.register(Efecto,EfectoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Actividades,ActividadesAdmin)
