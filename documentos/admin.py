from django.contrib import admin
from .models import *
# Register your models here.

class InlineDocumentos_Inline(admin.TabularInline):
    model = InlineDocumentos
    extra = 1

class DocumentosAdmin(admin.ModelAdmin):
    inlines = [InlineDocumentos_Inline]

admin.site.register(Documentos,DocumentosAdmin)
