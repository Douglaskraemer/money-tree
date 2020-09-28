from django.urls import path

# importar as views que criamos na cadastros/views.py
from .views import CategoriaCreate, DespesaCreate
from .views import CategoriaUpdate, DespesaUpdate
from .views import CategoriaDelete, DespesaDelete
from .views import CategoriaList, DespesaList

urlpatterns = [
    # CADASTRAR
    path('cadastrar/categoria/', CategoriaCreate.as_view(),
         name='cadastrar-categoria'),
    path('cadastrar/despesa/', DespesaCreate.as_view(),
         name='cadastrar-despesa'),

    # EDITAR
    path('editar/categoria/<int:pk>/',
         CategoriaUpdate.as_view(), name='editar-categoria'),
    path('editar/despesa/<int:pk>/',
         DespesaUpdate.as_view(), name='editar-despesa'),

    # EXCLUIR
    path('excluir/categoria/<int:pk>/',
         CategoriaDelete.as_view(), name='excluir-categoria'),
    path('excluir/despesa/<int:pk>/',
         DespesaDelete.as_view(), name='excluir-despesa'),

    # LISTAR
    path('listar/categoria/', CategoriaList.as_view(), name='listar-categoria'),
    path('listar/despesa/', DespesaList.as_view(), name='listar-despesa'),
]
