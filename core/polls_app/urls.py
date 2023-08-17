from django.urls import path
from .views import (
    EncuestaListCreateView,
    EncuestaRetrieveUpdateDeleteView,
    OpcionListCreateView,
    VotoCreateView,
)

urlpatterns = [
    path('encuestas/', EncuestaListCreateView.as_view(), name='encuesta-list-create'),
    path('encuestas/<int:pk>/', EncuestaRetrieveUpdateDeleteView.as_view(), name='encuesta-retrieve-update-delete'),
    path('opciones/', OpcionListCreateView.as_view(), name='opcion-list-create'),
    path('votos/', VotoCreateView.as_view(), name='voto-create'),
]
