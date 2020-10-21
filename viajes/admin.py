from django.contrib import admin
from .models import *

# Register your models here.
class InlineViaje_Inline(admin.TabularInline):
    model = InlineViaje
    extra = 1

class ViajesAdmin(admin.ModelAdmin):
    inlines = [InlineViaje_Inline]

admin.site.register(Viajes,ViajesAdmin)
