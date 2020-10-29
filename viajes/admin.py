from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
class InlineViaje_Inline(admin.TabularInline):
	model = InlineViaje
	extra = 1
	form = InlineViajeForm

class ViajesAdmin(admin.ModelAdmin):
	inlines = [InlineViaje_Inline]
	list_display = ('proyecto','anio')
	list_filter = ('proyecto',)

	def get_queryset(self, request):
		if request.user.is_superuser:
			return Viajes.objects.all()
		return Viajes.objects.filter(usuario=request.user)

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
		return super(ViajesAdmin, self).get_form(request, obj=None, **kwargs)

admin.site.register(Viajes,ViajesAdmin)
