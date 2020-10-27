# -*- coding: UTF-8 -*-
from django.db import models
from .models import *
from django import forms

class InlineViajeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InlineViajeForm, self).__init__(*args, **kwargs)
        self.fields['gastos_boletos'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['gastos_combustibles'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['gastos_alojamiento'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['gastos_diarios'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
        self.fields['otros_gastos'] = forms.FloatField(widget=forms.TextInput(attrs={'size':'7'}))
