from django.urls import path
from .views import (
    EncuestaListCreateView,
    EncuestaDetailView,
    OpcionListCreateView,
    VotoCreateView,
)

urlpatterns = [
    path('encuestas/', EncuestaListCreateView.as_view(), name='encuesta-list-create'),
    path('encuestas/<int:pk>/', EncuestaDetailView.as_view(), name='encuesta-create'),
    path('opciones/', OpcionListCreateView.as_view(), name='opcion-list-create'),
    path('votos/', VotoCreateView.as_view(), name='voto-create'),
]
