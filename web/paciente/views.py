from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Paciente


# Create your views here.
class PacienteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Paciente
    fields = '__all__'
    template_name = 'paciente/cadastrar.html'
    success_url = '/paciente/listar/'


class PacienteListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Paciente
    template_name = 'paciente/listar.html'
    success_url = '/paciente/listar/'


class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Paciente
    fields = '__all__'
    template_name = 'paciente/alterar.html'
    success_url = '/paciente/listar/'


class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Paciente
    template_name = 'paciente/deletar.html'
    success_url = '/paciente/listar/'
