from django.contrib import admin
from .models import Categoria, Contato, Despesa


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'data_criacao', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')
    list_editable = ('telefone', 'mostrar')


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor_total',
                    'vencimento', 'categoria', 'status_pagamento')
    list_per_page = 10
    search_fields = ('descricao',)
    list_editable = ('valor_total', 'categoria', 'status_pagamento')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Despesa, DespesaAdmin)
