from django import forms
from .models import Agendamento


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'descricao', 'status', 'pais', 'medico', 'paciente']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'medico': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.TextInput(attrs={'class': 'form-control'}),
        }
