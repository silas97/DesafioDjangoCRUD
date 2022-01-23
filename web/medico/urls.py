from django.urls import path

from .views import IndexTemplateView, DetalhesTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('mostrar/', DetalhesTemplateView.as_view(), name='detalhes'),
]
