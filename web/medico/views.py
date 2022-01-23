from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'medico/index.html'


class DetalhesTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    template_name = 'medico/detalhes.html'
