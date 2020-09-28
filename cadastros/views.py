from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Categoria, Despesa
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de categoria"
        context['botao'] = "Cadastrar"
        return context


class DespesaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Despesa
    fields = ['descricao', 'valor_total', 'vencimento', 'categoria', ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def form_valid(self, form):

        # Antes do super não foi criado o objeto nem salvo no banco
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # Depois do super(desta linha acima) foi criado objeto
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de despesas"
        context['botao'] = "Cadastrar"

        return context

#################### UPDATE ####################


class CategoriaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar categoria"
        context['botao'] = "Salvar"

        return context


class DespesaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Despesa
    fields = ['descricao', 'valor_total', 'vencimento', 'categoria', ]
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-despesa')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Despesa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar despesas"
        context['botao'] = "Salvar"

        return context


#################### DELETE ####################


class CategoriaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Categoria
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy('listar-despesa')


class DespesaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('users-login')
    group_required = u"Administrador"
    model = Despesa
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy('listar-despesa')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Despesa, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

#################### LIST ####################


class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    model = Categoria
    template_name = "cadastros/listas/categoria.html"


class DespesaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('users-login')
    model = Despesa
    template_name = "cadastros/listas/despesa.html"

    def get_queryset(self):
        self.object_list = Despesa.objects.filter(usuario=self.request.user)
        return self.object_list
