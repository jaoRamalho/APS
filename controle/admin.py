from django.contrib import admin
from controle.models import PontoDeAcesso, Cliente, Conta

class PontoDeAcessoAdmin(admin.ModelAdmin):
    list_display = ['id', 'codigo', 'cliente']
 

class ClieteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone']

class ContaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data_vencimento']


admin.site.register(PontoDeAcesso, PontoDeAcessoAdmin)
admin.site.register(Cliente, ClieteAdmin)
admin.site.register(Conta, ContaAdmin)
