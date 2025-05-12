from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'plano', 'devendo']
        widgets = {
            'plano': forms.Select(attrs={'class': 'rounded-xl px-3 py-1 border border-green-400 text-green-800'}),
            'devendo': forms.CheckboxInput(attrs={'class': 'h-5 w-5 text-green-600'}),
        }
