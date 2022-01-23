from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Agendamento


# Create your views here.
class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Agendamento
    fields = '__all__'
    template_name = 'agendamento/cadastrar.html'
    success_url = '/agendamento/listar/'


class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Agendamento
    fields = '__all__'
    template_name = 'agendamento/alterar.html'
    success_url = '/agendamento/listar/'


class AgendamentoListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Agendamento
    template_name = 'agendamento/listar.html'
    success_url = '/agendamento/listar/'


class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Agendamento
    template_name = 'agendamento/deletar.html'
    success_url = '/agendamento/listar/'
