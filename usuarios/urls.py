from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UsuarioCreate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/form-login2.html'
    ), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
]
