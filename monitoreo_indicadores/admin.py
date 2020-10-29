from django.contrib import admin
from .models import *
from django.forms import Textarea

# Register your models here.

# class ObjInd1_Inline(admin.TabularInline):
# 	model = ObjInd1
# 	extra = 1
#
# class ObjInd2_Inline(admin.TabularInline):
# 	model = ObjInd2
# 	extra = 1
#
# class ObjInd3_Inline(admin.TabularInline):
# 	model = ObjInd3
# 	extra = 1
# 	formfield_overrides = {
# 		models.TextField: {'widget': Textarea(
# 						   attrs={'rows': 1,
# 								  'cols': 40,
# 								  'style': 'height: 150px;resize:none;',})},
# 	}
#
# class ObjInd4_Inline(admin.TabularInline):
# 	model = ObjInd4
# 	extra = 1
#
# 	formfield_overrides = {
# 		models.TextField: {'widget': Textarea(
# 						   attrs={'rows': 1,
# 								  'cols': 40,
# 								  'style': 'height: 150px;resize:none;',})},
# 	}

class IndicadoresObjetivosInline_Inline(admin.TabularInline):
	model = IndicadoresObjetivosInline
	extra = 1
	formfield_overrides = {
			models.TextField: {'widget': Textarea(
							   attrs={'rows': 1,
									  'cols': 40,
									  'style': 'height: 150px;resize:none;',})},
		}

class IndObjetivosAdmin(admin.ModelAdmin):
	inlines = [IndicadoresObjetivosInline_Inline,]
	list_display = ('proyecto','indicador')
	list_filter = ('proyecto',)
	# class Media:
	# 	js = ('js/admin.js',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return IndObjetivos.objects.all()
		return IndObjetivos.objects.filter(usuario=request.user)

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
		return super(IndObjetivosAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(IndObjetivos,IndObjetivosAdmin)

#efectos
# class IndEfecto1_1_Inline(admin.TabularInline):
# 	model = IndEfecto1_1
# 	extra = 1
#
# class IndEfecto1_2_Inline(admin.TabularInline):
# 	model = IndEfecto1_2
# 	extra = 1
#
# class IndEfecto2_1_Inline(admin.TabularInline):
# 	model = IndEfecto2_1
# 	extra = 1
#
# 	formfield_overrides = {
# 		models.TextField: {'widget': Textarea(
# 						   attrs={'rows': 1,
# 								  'cols': 40,
# 								  'style': 'height: 150px;resize:none;',})},
# 	}

class IndicadoresEfectosInline_Inline(admin.TabularInline):
	model = IndicadoresEfectosInline
	extra = 1
	formfield_overrides = {
		models.TextField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 40,
								  'style': 'height: 150px;resize:none;',})},
	}

class IndEfectosAdmin(admin.ModelAdmin):
	inlines = [IndicadoresEfectosInline_Inline,]
	list_display = ('proyecto','indicador')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return IndEfectos.objects.all()
		return IndEfectos.objects.filter(usuario=request.user)

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
		return super(IndEfectosAdmin, self).get_form(request, obj=None, **kwargs)

	# class Media:
	# 	js = ('js/efectos.js',)

admin.site.register(IndEfectos,IndEfectosAdmin)

#productos
# class IndProducto1_1_1_Inline(admin.TabularInline):
# 	model = IndProducto1_1_1
# 	extra = 1
#
# class IndProducto1_1_2_Inline(admin.TabularInline):
# 	model = IndProducto1_1_2
# 	extra = 1
#
# class IndProducto1_1_3_Inline(admin.TabularInline):
# 	model = IndProducto1_1_3
# 	extra = 1
#
# class IndProducto1_1_3_Inline(admin.TabularInline):
# 	model = IndProducto1_1_3
# 	extra = 1
#
# class IndProducto1_2_1_Inline(admin.TabularInline):
# 	model = IndProducto1_2_1
# 	extra = 1
#
# class IndProducto1_2_2_Inline(admin.TabularInline):
# 	model = IndProducto1_2_2
# 	extra = 1
#
# class IndProducto1_2_3_Inline(admin.TabularInline):
# 	model = IndProducto1_2_3
# 	extra = 1
#
# class IndProducto1_2_4_Inline(admin.TabularInline):
# 	model = IndProducto1_2_4
# 	extra = 1
#
# class IndProducto1_2_5_Inline(admin.TabularInline):
# 	model = IndProducto1_2_5
# 	extra = 1
#
# class IndProducto1_3_1_Inline(admin.TabularInline):
# 	model = IndProducto1_3_1
# 	extra = 1
#
# class IndProducto1_3_2_Inline(admin.TabularInline):
# 	model = IndProducto1_3_2
# 	extra = 1
#
# class IndProducto1_3_3_Inline(admin.TabularInline):
# 	model = IndProducto1_3_3
# 	extra = 1
#
# class IndProducto1_4_1_Inline(admin.TabularInline):
# 	model = IndProducto1_4_1
# 	extra = 1
#
# class IndProducto1_4_2_Inline(admin.TabularInline):
# 	model = IndProducto1_4_2
# 	extra = 1
#
# class IndProducto1_4_3_Inline(admin.TabularInline):
# 	model = IndProducto1_4_3
# 	extra = 1
#
# class IndProducto1_4_4_Inline(admin.TabularInline):
# 	model = IndProducto1_4_4
# 	extra = 1
#
# class IndProducto2_5_1_Inline(admin.TabularInline):
# 	model = IndProducto2_5_1
# 	extra = 1
#
# class IndProducto2_5_2_Inline(admin.TabularInline):
# 	model = IndProducto2_5_2
# 	extra = 1
#
# class IndProducto2_6_1_Inline(admin.TabularInline):
# 	model = IndProducto2_6_1
# 	extra = 1
#
# class IndProducto2_6_2_Inline(admin.TabularInline):
# 	model = IndProducto2_6_2
# 	extra = 1
#
# class IndProducto2_7_1_Inline(admin.TabularInline):
# 	model = IndProducto2_7_1
# 	extra = 1
#
# class IndProducto2_7_2_Inline(admin.TabularInline):
# 	model = IndProducto2_7_2
# 	extra = 1

class IndicadoresProductosInline_Inline(admin.TabularInline):
	model = IndicadoresProductosInline
	extra = 1
	formfield_overrides = {
		models.TextField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 40,
								  'style': 'height: 150px;resize:none;',})},
	}

class IndProductosAdmin(admin.ModelAdmin):
	inlines = [IndicadoresProductosInline_Inline,]
	list_display = ('proyecto','indicador')
	list_filter = ('proyecto',)
	# class Media:
	# 	js = ('js/producto.js',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return IndProductos.objects.all()
		return IndProductos.objects.filter(usuario=request.user)

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
		return super(IndProductosAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(IndProductos,IndProductosAdmin)
