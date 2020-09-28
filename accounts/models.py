from django.db import models
from gerenciador.models import Despesa
from django import forms


class FormDespesa(forms.ModelForm):
    class Meta:
        model = Despesa
        exclude = ('status_pagamento',)
