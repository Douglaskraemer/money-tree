from accounts.models import FormDespesa
from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):

    # Se nada for postado exibe o formulário
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    """Aqui foi criado as variaveis q vão receber 
    os atributos, respectivos de cada campo (name) no form do login.html"""
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    # Neste comando, É feita uma comparação(autenticação)
    # Não estou logando ele ainda
    user = auth.authenticate(request, username=usuario, password=senha)

    # Se não for user não vou validar
    if not user:
        return render(request, 'accounts/login.html')

    # Se for entra no else e faz login
    else:
        # Aqui faço o login usando o a variavel user que criei
        auth.login(request, user)
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    # teste para ver se esta NADA POSTADO,pra ele não postar campos em branco
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    """Aqui foi criado as variaveis q vão receber 
    os atributos, respectivos de cada campo (name) no form do cadastro.html"""
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    # Validação, nenhum campo pode estar vazio
    if not nome or not sobrenome or not email or not usuario or\
            not senha or not senha2:
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        return render(request, 'accounts/cadastro.html')

    # COMEÇA AS VALIDACÕES PARA OS CAMPOS DA PAGINA CADASTRO

    # Senha não pode ser menor que 6 digitos
    if len(senha) < 6:
        return render(request, 'accounts/cadastro.html')

    # Usuário não pode ser menor que 6 digitos
    if len(usuario) < 6:
        return render(request, 'accounts/cadastro.html')

    # As senhas não podem ser diferentes
    if senha != senha2:
        return render(request, 'accounts/cadastro.html')

    # Verifica se o usuario já exite
    if User.objects.filter(username=usuario).exists():
        return render(request, 'accounts/cadastro.html')

    # Verifica se o email já exite
    if User.objects.filter(email=email).exists():
        return render(request, 'accounts/cadastro.html')

    # REGISTRO DE USUARIO SE FAZ COM ESSE COMANDO
    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()

    # REDIRECIONA PARA PAGINA LOGIN
    return redirect('login')

# Se o usuario não estiver logado redireciona para login


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormDespesa()
        return render(request, 'accounts/dashboard.html', {
            'form': form
        })
    form = FormDespesa(request.POST, request.FILES)

    if not form.is_valid():
        form = FormDespesa(request.POST)
        return render(request, 'accounts/dashboard.html', {
            'form': form
        })

    form.save()
    return redirect('dashboard')
