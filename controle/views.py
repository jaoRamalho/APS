from django.shortcuts import render, redirect
from controle.models import Cliente, OrdemDeServico, Equipe, Perfil, User

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .decorators import equipes_permitidas

from django.contrib.auth.forms import AuthenticationForm

from .forms import ClienteForm, OrdemDeServicoForm

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



#views de clientes
@login_required
@equipes_permitidas('tela_clientes')
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
    
    #filtros
    cliente_nome = request.GET.get('nome')
    plano = request.GET.get('plano')
    devendo = request.GET.get('devendo')

    filtros = {}

    if cliente_nome:
        filtros['nome__icontains'] = cliente_nome

    if plano:
        filtros['plano'] = plano

    if devendo == 'true':
        filtros['devendo'] = True
    elif devendo == 'false':
        filtros['devendo'] = False


    clientes = Cliente.objects.filter(**filtros)
    return render(request, 'clientes.html',{'clientes': clientes, 'planos_choices': Cliente.PLANOS})

@login_required
@equipes_permitidas('tela_clientes')
def adicionar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')  # ajuste conforme sua URL
    else:
        form = ClienteForm()

    return render(request, 'adicionar_cliente.html', {'form': form})





#views de ordem de serviço 
@login_required
@equipes_permitidas('tela_ordens_de_servico')
def listar_OS(request):
    if request.method == "POST":
        os_id = request.POST.get("atualizar")
        os = OrdemDeServico.objects.get(id=os_id)
        os.cliente = Cliente.objects.get(id = request.POST.get(f'cliente_{os_id}'))
        os.tipo = request.POST.get(f'tipo_{os_id}')
        os.prioridade = request.POST.get(f'prioridade_{os_id}')
        os.prazo = request.POST.get(f'prazo_{os_id}')
        os.descricao = request.POST.get(f'descricao_{os_id}')
        os.status = request.POST.get(f'status_{os_id}')
        os.equipe = Equipe.objects.get(id = request.POST.get(f'equipe_{os_id}'))
        os.save()
        return redirect('listar_os')
    
    

    # Filtros de busca

    filtros = {}
    cliente_nome = request.GET.get('cliente')
    tipo = request.GET.get('tipo')
    prioridade = request.GET.get('prioridade')
    status = request.GET.get('status')
    prazo = request.GET.get('prazo')
    equipe = request.GET.get('equipe')

    if cliente_nome:
        filtros['cliente__nome__icontains'] = cliente_nome

    if tipo:
        filtros['tipo'] = tipo

    if prioridade:
        filtros['prioridade'] = prioridade

    if status:
        filtros['status'] = status

    if prazo:
        filtros['prazo'] = prazo

    if equipe:
        filtros['equipe__id'] = equipe

    ordens = OrdemDeServico.objects.filter(**filtros)

    clientes = Cliente.objects.all()
    equipes = Equipe.objects.all()
    return render(request, 'ordem_servico.html',{
        'ordens': ordens, 'tipos_choices': OrdemDeServico.TIPOS_OS,
        'prioridades_choices': OrdemDeServico.TIPOS_PRIORIDADE, 
        'status_choices': OrdemDeServico.STATUS,
        'clientes' : clientes,
        'equipes' : equipes
    })

@login_required
@equipes_permitidas('tela_ordens_de_servico')
def adicionar_OS(request):
    if request.method == 'POST':
        form = OrdemDeServicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_os') 
    else:
        form = OrdemDeServicoForm()

    return render(request, 'adicionar_os.html', {'form': form})



#views de funcionarios 
@login_required
@equipes_permitidas('tela_funcionarios')
def listar_funcionarios(request):
    if request.method == "POST":
        perfil_id = request.POST.get("atualizar")
        perfil = Perfil.objects.get(id=perfil_id)
        perfil.equipe = Equipe.objects.get(id = request.POST.get(f'equipe_{perfil_id}'))
        perfil.cpf = request.POST.get(f'cpf_{perfil_id}')
        perfil.conta_bancaria = request.POST.get(f'conta_{perfil_id}')
        perfil.save()
        return redirect('listar_funcionarios')
    
    #filtros
    usuario = request.GET.get('usuario')
    equipe_id = request.GET.get('equipe')
    cpf = request.GET.get('cpf')
    conta_bancaria = request.GET.get('conta_bancaria')

    filtros = {}

    if usuario:
        filtros['usuario__username__icontains'] = usuario

    if equipe_id:
        filtros['equipe_id'] = equipe_id  

    if cpf:
        filtros['cpf__icontains'] = cpf

    if conta_bancaria:
        filtros['conta_bancaria__icontains'] = conta_bancaria


    perfils = Perfil.objects.filter(**filtros)
    equipes = Equipe.objects.all()
    return render(request, 'funcionarios.html',{
        'perfils': perfils,
        'equipes' : equipes
    })