from django.urls import path

from controle import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('acesso_negado/', views.acesso_negado, name='acesso_negado'),
]
