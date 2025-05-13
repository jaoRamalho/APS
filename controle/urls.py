from django.urls import path

from controle import views

urlpatterns = [
    path('', views.listar_clientes, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('acesso_negado/', views.acesso_negado, name='acesso_negado'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('ordens-servico/', views.listar_OS, name='listar_os'),
    path('ordens-servico/adicionar', views.adicionar_OS, name='adicionar_os'),
]
