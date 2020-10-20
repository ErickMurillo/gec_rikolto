from django.contrib import admin
from .models import *
import nested_admin

# Register your models here.
class ProductoProyecto_Inline(nested_admin.NestedTabularInline):
    model = ProductoProyecto
    extra = 1

class InlineProyecto_Inline(nested_admin.NestedTabularInline):
    model = InlineProyecto
    extra = 1
    inlines = [ProductoProyecto_Inline,]

class ProyectosFinanciadosAdmin(nested_admin.NestedModelAdmin):
    inlines = [InlineProyecto_Inline,]

admin.site.register(ProyectosFinanciados,ProyectosFinanciadosAdmin)
