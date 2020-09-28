from django.contrib import admin

# importar Classes
from .models import Categoria, Despesa

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Despesa)
