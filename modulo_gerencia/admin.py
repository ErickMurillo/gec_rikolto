from django.contrib import admin
from .models import *

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
	filter_horizontal = ['financiadores','aliados',]

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Proyecto.objects.all()
		return Proyecto.objects.filter(usuario=request.user)

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
		return super(ProyectoAdmin, self).get_form(request, obj=None, **kwargs)

class IndicadoresObjetivos_Inline(admin.TabularInline):
	model = IndicadoresObjetivos
	extra = 1

class ObjetivoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresObjetivos_Inline,]
	list_display = ('proyecto','identificador','descripcion')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Objetivo.objects.all()
		return Objetivo.objects.filter(usuario=request.user)

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
		return super(ObjetivoAdmin, self).get_form(request, obj=None, **kwargs)

class IndicadoresEfectos_Inline(admin.TabularInline):
	model = IndicadoresEfectos
	extra = 1

class EfectoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresEfectos_Inline,]
	list_display = ('proyecto','identificador','descripcion')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Efecto.objects.all()
		return Efecto.objects.filter(usuario=request.user)

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
		return super(EfectoAdmin, self).get_form(request, obj=None, **kwargs)

class IndicadoresProductos_Inline(admin.TabularInline):
	model = IndicadoresProductos
	extra = 1

class ProductoAdmin(admin.ModelAdmin):
	inlines = [IndicadoresProductos_Inline,]
	list_display = ('proyecto','identificador','descripcion')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Producto.objects.all()
		return Producto.objects.filter(usuario=request.user)

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
		return super(ProductoAdmin, self).get_form(request, obj=None, **kwargs)

class ActividadesAdmin(admin.ModelAdmin):
	ordering = ['identificador','producto']
	search_fields = ['identificador','descripcion']
	list_display = ('proyecto','identificador','descripcion')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Actividades.objects.all()
		return Actividades.objects.filter(usuario=request.user)

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
		return super(ActividadesAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Objetivo,ObjetivoAdmin)
admin.site.register(Efecto,EfectoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Actividades,ActividadesAdmin)
