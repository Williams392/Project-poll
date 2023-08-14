from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Encuesta, Opcion, Voto
from .serializers import EncuestaSerializer, OpcionSerializer, VotoSerializer

class EncuestaListCreateView(generics.ListCreateAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

class EncuestaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Encuesta.objects.all()
    serializer_class = EncuestaSerializer

class OpcionListCreateView(generics.ListCreateAPIView):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

class VotoCreateView(generics.CreateAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer
