from django.contrib import admin
from .models import *
# Register your models here.

class InlineDocumentos_Inline(admin.TabularInline):
	model = InlineDocumentos
	extra = 1

class DocumentosAdmin(admin.ModelAdmin):
	inlines = [InlineDocumentos_Inline]
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Documentos.objects.all()
		return Documentos.objects.filter(usuario=request.user)

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
		return super(DocumentosAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(Documentos,DocumentosAdmin)
