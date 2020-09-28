from django.shortcuts import render, get_object_or_404, redirect
from .models import Despesa
from django.contrib.auth.decorators import login_required


def index(request):
    gerenciador = Despesa.objects.order_by('vencimento')
    return render(request, 'gerenciador/index.html', {
        'gerenciador': gerenciador
    })


def ver_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id)

    return render(request, 'gerenciador/ver_despesa.html', {
        'despesa': despesa
    })
