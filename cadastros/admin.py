from django.contrib import admin

# importar Classes
from .models import Categoria, Despesa


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor_total',
                    'vencimento', 'categoria', 'opcoes')
    list_per_page = 20
    search_fields = ('descricao',)
    list_editable = ('valor_total', 'categoria', 'opcoes')


# Register your models here.

admin.site.register(Categoria)
admin.site.register(Despesa, DespesaAdmin)
