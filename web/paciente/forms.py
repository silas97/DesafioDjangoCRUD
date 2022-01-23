from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'endereco',
                  'numero', 'cidade', 'uf', 'pais', 'cep']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
        }
