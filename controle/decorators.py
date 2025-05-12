from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import PaginaAcesso

def equipes_permitidas(nome_pagina):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            pagina = PaginaAcesso.objects.get(nome_pagina=nome_pagina)
            equipes_permitidas = pagina.equipes.all()
            user_equipes = request.user.perfil.equipe

            # Verifica se o usuário pertence a uma das equipes permitidas
            if user_equipes in equipes_permitidas:
                print(equipes_permitidas)
                print(user_equipes)

                return view_func(request, *args, **kwargs)
            return redirect('acesso_negado')  # Redireciona para página de erro
        return _wrapped_view
    return decorator
