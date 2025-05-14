from django.core.management.base import BaseCommand
from controle.models import Equipe, PaginaAcesso, Perfil, User

class Command(BaseCommand):
    help = 'Cria equipes, páginas e associa as equipes às páginas automaticamente'

    def handle(self, *args, **kwargs):
        # Criar equipes
        self.stdout.write(self.style.NOTICE('Criando equipes...'))
        equipe_1 = Equipe.objects.create(nome='administracao')
        equipe_2 = Equipe.objects.create(nome='atendimento')
        equipe_3 = Equipe.objects.create(nome='instalacao')
        equipe_4 = Equipe.objects.create(nome='suporte')


        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_1.nome}'))
        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_2.nome}'))
        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_3.nome}'))
        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_4.nome}'))


        # Criar páginas
        self.stdout.write(self.style.NOTICE('Criando páginas...'))
        pagina_clientes = PaginaAcesso.objects.create(nome_pagina='tela_clientes')
        pagina_os = PaginaAcesso.objects.create(nome_pagina='tela_ordens_de_servico')
        pagina_funcionarios = PaginaAcesso.objects.create(nome_pagina='tela_funcionarios')

        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_clientes.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_os.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_funcionarios.nome_pagina}'))

        # Associar equipes às páginas
        self.stdout.write(self.style.NOTICE('Associando equipes às páginas...'))
        pagina_clientes.equipes.add(equipe_1, equipe_2)  # Associar 'tela_clientes' com 'atendimento' e 'administracao'
        pagina_os.equipes.add(equipe_1, equipe_2, equipe_3, equipe_4)  # 'tela_ordens_de_servico' com todas equipes
        pagina_funcionarios.equipes.add(equipe_1)  # 'administracao' com 'tela_funcionarios'

        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_clientes.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_os.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_funcionarios.nome_pagina}'))

        #criando usuario Perfil username:admin senha:admin
        if not User.objects.filter(username='admin').exists():
            usuario = User.objects.create_superuser(username='admin', password='admin')
            Perfil.objects.create(usuario=usuario, equipe=equipe_1)
            self.stdout.write(self.style.SUCCESS('Usuário e perfil criados com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING('Usuário já existe.'))



        self.stdout.write(self.style.SUCCESS('Seed finalizado com sucesso!'))
