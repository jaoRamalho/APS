from django.shortcuts import render

from controle.models import PontoDeAcesso 

def index(request):
    
    pontos_acesso = PontoDeAcesso.objects.filter(ativo=True)

    dados = {
        'ponto_acesso' : pontos_acesso
    }

    return render(request, 'index.html', dados) 