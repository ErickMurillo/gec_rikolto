from django.contrib import admin
from .models import *

# Register your models here.
class InlineContrapartida_Inline(admin.TabularInline):
    model = InlineContrapartida
    extra = 1

class ContrapartidaAdmin(admin.ModelAdmin):
    inlines = [InlineContrapartida_Inline]

admin.site.register(Contrapartida,ContrapartidaAdmin)
