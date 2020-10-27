# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import AutocompleteSelect

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
        self.fields['monto_presupuestado'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['monto_semestre_1'] = forms.FloatField(required=False,widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['monto_final_anio'] = forms.FloatField(required=False,widget=forms.TextInput(attrs={'size':'7'}))

class ActividadesPOAForm(forms.ModelForm):
	class Meta:
		widgets = {
			'actividad': AutocompleteSelect(
				ActividadesPOA._meta.get_field('actividad').remote_field,
				admin.site,
				attrs={'style': 'width: 400px'}
			),
		}
