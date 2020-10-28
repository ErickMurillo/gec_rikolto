from django.contrib import admin
from .models import *
from django.forms import Textarea

# Register your models here.

class ObjInd1_Inline(admin.TabularInline):
	model = ObjInd1
	extra = 1

class ObjInd2_Inline(admin.TabularInline):
	model = ObjInd2
	extra = 1

class ObjInd3_Inline(admin.TabularInline):
	model = ObjInd3
	extra = 1
	formfield_overrides = {
		models.TextField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 40,
								  'style': 'height: 150px;resize:none;',})},
	}

class ObjInd4_Inline(admin.TabularInline):
	model = ObjInd4
	extra = 1

	formfield_overrides = {
		models.TextField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 40,
								  'style': 'height: 150px;resize:none;',})},
	}


class IndObjetivosAdmin(admin.ModelAdmin):
	inlines = [ObjInd1_Inline,ObjInd2_Inline,ObjInd3_Inline,ObjInd4_Inline,]

	class Media:
		js = ('js/admin.js',)

admin.site.register(IndObjetivos,IndObjetivosAdmin)

#efectos
class IndEfecto1_1_Inline(admin.TabularInline):
	model = IndEfecto1_1
	extra = 1

class IndEfecto1_2_Inline(admin.TabularInline):
	model = IndEfecto1_2
	extra = 1

class IndEfecto2_1_Inline(admin.TabularInline):
	model = IndEfecto2_1
	extra = 1

	formfield_overrides = {
		models.TextField: {'widget': Textarea(
						   attrs={'rows': 1,
								  'cols': 40,
								  'style': 'height: 150px;resize:none;',})},
	}

class IndEfectosAdmin(admin.ModelAdmin):
	inlines = [IndEfecto1_1_Inline,IndEfecto1_2_Inline,IndEfecto2_1_Inline]

	class Media:
		js = ('js/efectos.js',)

admin.site.register(IndEfectos,IndEfectosAdmin)

#productos
class IndProducto1_1_1_Inline(admin.TabularInline):
	model = IndProducto1_1_1
	extra = 1

class IndProducto1_1_2_Inline(admin.TabularInline):
	model = IndProducto1_1_2
	extra = 1

class IndProducto1_1_3_Inline(admin.TabularInline):
	model = IndProducto1_1_3
	extra = 1

class IndProducto1_1_3_Inline(admin.TabularInline):
	model = IndProducto1_1_3
	extra = 1

class IndProducto1_2_1_Inline(admin.TabularInline):
	model = IndProducto1_2_1
	extra = 1

class IndProducto1_2_2_Inline(admin.TabularInline):
	model = IndProducto1_2_2
	extra = 1

class IndProducto1_2_3_Inline(admin.TabularInline):
	model = IndProducto1_2_3
	extra = 1

class IndProducto1_2_4_Inline(admin.TabularInline):
	model = IndProducto1_2_4
	extra = 1

class IndProducto1_2_5_Inline(admin.TabularInline):
	model = IndProducto1_2_5
	extra = 1

class IndProducto1_3_1_Inline(admin.TabularInline):
	model = IndProducto1_3_1
	extra = 1

class IndProducto1_3_2_Inline(admin.TabularInline):
	model = IndProducto1_3_2
	extra = 1

class IndProducto1_3_3_Inline(admin.TabularInline):
	model = IndProducto1_3_3
	extra = 1

class IndProducto1_4_1_Inline(admin.TabularInline):
	model = IndProducto1_4_1
	extra = 1

class IndProducto1_4_2_Inline(admin.TabularInline):
	model = IndProducto1_4_2
	extra = 1

class IndProducto1_4_3_Inline(admin.TabularInline):
	model = IndProducto1_4_3
	extra = 1

class IndProducto1_4_4_Inline(admin.TabularInline):
	model = IndProducto1_4_4
	extra = 1

class IndProducto2_5_1_Inline(admin.TabularInline):
	model = IndProducto2_5_1
	extra = 1

class IndProducto2_5_2_Inline(admin.TabularInline):
	model = IndProducto2_5_2
	extra = 1

class IndProducto2_6_1_Inline(admin.TabularInline):
	model = IndProducto2_6_1
	extra = 1

class IndProducto2_6_2_Inline(admin.TabularInline):
	model = IndProducto2_6_2
	extra = 1

class IndProducto2_7_1_Inline(admin.TabularInline):
	model = IndProducto2_7_1
	extra = 1

class IndProducto2_7_2_Inline(admin.TabularInline):
	model = IndProducto2_7_2
	extra = 1

class IndProductosAdmin(admin.ModelAdmin):
	inlines = [IndProducto1_1_1_Inline,IndProducto1_1_2_Inline,IndProducto1_1_3_Inline,
				IndProducto1_2_1_Inline,IndProducto1_2_2_Inline,IndProducto1_2_3_Inline,IndProducto1_2_4_Inline,IndProducto1_2_5_Inline,
				IndProducto1_3_1_Inline,IndProducto1_3_2_Inline,IndProducto1_3_3_Inline,
				IndProducto1_4_1_Inline,IndProducto1_4_2_Inline,IndProducto1_4_3_Inline,IndProducto1_4_4_Inline,
				IndProducto2_5_1_Inline,IndProducto2_5_2_Inline,
				IndProducto2_6_1_Inline,IndProducto2_6_2_Inline,
				IndProducto2_7_1_Inline,IndProducto2_7_2_Inline]
	class Media:
		js = ('js/producto.js',)

admin.site.register(IndProductos,IndProductosAdmin)
