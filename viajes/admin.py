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

admin.site.register(Viajes,ViajesAdmin)
