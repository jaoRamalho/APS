from django.shortcuts import render
from controle.models import PontoDeAcesso

from django.contrib.auth.decorators import login_required

from .decorators import equipes_permitidas

@equipes_permitidas('index')
def index(request):
    
    pontos_acesso = PontoDeAcesso.objects.filter(status=True)

    dados = {
        'pontos_acesso' : pontos_acesso
    }

    return render(request, 'index.html', dados) 

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirecione usuários logados

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redireciona após login bem-sucedido
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@equipes_permitidas('Financeiro')
def pagina_financeiro(request):
    return render(request, 'financeiro.html')

@equipes_permitidas('Suporte')
def pagina_suporte(request):
    return render(request, 'suporte.html')

def acesso_negado(request):
    return render(request, 'acesso_negado.html')