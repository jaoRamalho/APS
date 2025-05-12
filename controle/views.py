from django.shortcuts import render
from controle.models import PontoDeAcesso, Cliente

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

def acesso_negado(request):
    return render(request, 'acesso_negado.html')


def listar_clientes(request):
    if request.method == "POST":
        cliente_id = request.POST.get("atualizar")
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.nome = request.POST.get(f'nome_{cliente_id}')
        cliente.email = request.POST.get(f'email_{cliente_id}')
        cliente.telefone = request.POST.get(f'telefone_{cliente_id}')
        cliente.endereco = request.POST.get(f'endereco_{cliente_id}')
        cliente.plano = request.POST.get(f'plano_{cliente_id}')
        cliente.devendo = f'devendo_{cliente_id}' in request.POST
        cliente.save()
        return redirect('listar_clientes')  # redireciona para evitar reenvio do formulário
    


    clientes = Cliente.objects.all()
    return render(request, 'clientes.html',{'clientes': clientes, 'planos_choices': Cliente.PLANOS})

from .forms import ClienteForm

def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # ajuste conforme sua URL
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})
