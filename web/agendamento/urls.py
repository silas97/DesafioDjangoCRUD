from django.urls import path
from .views import AgendamentoCreateView, AgendamentoUpdateView, AgendamentoDeleteView, AgendamentoListView

urlpatterns = [
    path('cadastrar/', AgendamentoCreateView.as_view(), name='cadastrar_agendamento'),
    path('listar/', AgendamentoListView.as_view(), name='listar_agendamentos'),
    path('alterar/<int:pk>/', AgendamentoUpdateView.as_view(), name='alterar_agendamento'),
    path('apagar/<int:pk>/', AgendamentoDeleteView.as_view(), name='apagar_agendamento'),
]
