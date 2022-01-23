from django.urls import path
from .views import PacienteCreateView, PacienteUpdateView, PacienteDeleteView, PacienteListView

urlpatterns = [
    path('cadastrar/', PacienteCreateView.as_view(), name='cadastrar_paciente'),
    path('listar/', PacienteListView.as_view(), name='listar_pacientes'),
    path('alterar/<int:pk>/', PacienteUpdateView.as_view(), name='alterar_paciente'),
    path('apagar/<int:pk>/', PacienteDeleteView.as_view(), name='apagar_paciente'),
]
