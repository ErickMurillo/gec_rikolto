# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms

def anios():
    anio_poa = Poa.objects.filter(proyecto = id).values_list('anio',flat=True).distinct()
    return anio_poa
    
class FiltroAnio(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FiltroAnio, self).__init__(*args, **kwargs)
        self.fields['anio'] = forms.ChoiceField(label=u'Años',queryset=anios())

class SubActividadesPOAAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubActividadesPOAAdminForm, self).__init__(*args, **kwargs)
        self.fields['identificador'] = forms.CharField(widget=forms.TextInput(attrs={'size':'5'}))
        self.fields['monto_presupuestado'] = forms.IntegerField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['monto_semestre_1'] = forms.IntegerField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['monto_final_anio'] = forms.IntegerField(widget=forms.TextInput(attrs={'size':'7'}))
        