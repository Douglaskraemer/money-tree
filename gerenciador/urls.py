from django.urls import path
from . import views

urlpatterns = [
    #path('<int:despesa_id>', views.deletar_post, name='deletar-post'),
    path('', views.index, name='index'),
    path('<int:despesa_id>', views.ver_despesa, name='ver-despesa'),
]
