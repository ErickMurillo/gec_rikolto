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