from django.contrib import admin
from .models import *

# Register your models here.
class InlineContrapartida_Inline(admin.TabularInline):
	model = InlineContrapartida
	extra = 1

class ContrapartidaAdmin(admin.ModelAdmin):
	inlines = [InlineContrapartida_Inline]
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Contrapartida.objects.all()
		return Contrapartida.objects.filter(usuario=request.user)

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
		return super(ContrapartidaAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(Contrapartida,ContrapartidaAdmin)
