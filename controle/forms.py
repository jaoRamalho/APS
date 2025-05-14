from django import forms
from .models import Cliente, OrdemDeServico, Perfil, User, Equipe

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'plano', 'devendo']
        widgets = {
            'plano': forms.Select(attrs={'class': 'rounded-xl px-3 py-1 border border-green-400 text-green-800'}),
            'devendo': forms.CheckboxInput(attrs={'class': 'h-5 w-5 text-green-600'}),
        }



class OrdemDeServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = ['cliente', 'tipo', 'prioridade', 'prazo', 'descricao', 'status', 'equipe']


# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Equipe

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['usuario', 'equipe', 'cpf', 'conta_bancaria']
    
    # Campos para criação de usuário
    usuario = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), required=True, empty_label="Selecione a equipe")
    cpf = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={'placeholder': 'Digite o CPF'}))
    conta_bancaria = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={'placeholder': 'Digite a conta bancária'}))

    def save(self, commit=True):
        # Primeiro cria o usuário
        user = User.objects.create_user(
            username=self.cleaned_data['usuario'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']  # A senha será automaticamente processada
        )
        
        # Cria o perfil associado ao usuário
        perfil = super().save(commit=False)
        perfil.usuario = user
        if commit:
            perfil.save()
        
        return perfil
