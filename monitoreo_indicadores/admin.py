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