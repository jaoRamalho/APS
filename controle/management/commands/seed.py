from django.core.management.base import BaseCommand
from controle.models import Equipe, PaginaAcesso

class Command(BaseCommand):
    help = 'Cria equipes, páginas e associa as equipes às páginas automaticamente'

    def handle(self, *args, **kwargs):
        # Criar equipes
        self.stdout.write(self.style.NOTICE('Criando equipes...'))
        equipe_1 = Equipe.objects.create(nome='Financeiro')
        equipe_2 = Equipe.objects.create(nome='Suporte')
        equipe_3 = Equipe.objects.create(nome='Marketing')

        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_1.nome}'))
        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_2.nome}'))
        self.stdout.write(self.style.SUCCESS(f'Equipe criada: {equipe_3.nome}'))

        # Criar páginas
        self.stdout.write(self.style.NOTICE('Criando páginas...'))
        pagina_financeiro = PaginaAcesso.objects.create(nome_pagina='Financeiro')
        pagina_suporte = PaginaAcesso.objects.create(nome_pagina='Suporte')
        pagina_marketing = PaginaAcesso.objects.create(nome_pagina='Marketing')

        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_financeiro.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_suporte.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Página criada: {pagina_marketing.nome_pagina}'))

        # Associar equipes às páginas
        self.stdout.write(self.style.NOTICE('Associando equipes às páginas...'))
        pagina_financeiro.equipes.add(equipe_1, equipe_2)  # Associar 'Financeiro' com 'Financeiro' e 'Suporte'
        pagina_suporte.equipes.add(equipe_2)  # 'Suporte' com 'Suporte'
        pagina_marketing.equipes.add(equipe_3)  # 'Marketing' com 'Marketing'

        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_financeiro.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_suporte.nome_pagina}'))
        self.stdout.write(self.style.SUCCESS(f'Equipes associadas à página: {pagina_marketing.nome_pagina}'))

        self.stdout.write(self.style.SUCCESS('Seed finalizado com sucesso!'))
