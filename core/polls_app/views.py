from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from .models import Encuesta, Opcion, Voto
from .serializers import EncuestaSerializer, OpcionSerializer, VotoSerializer

class EncuestaListCreateView(APIView):

    def get(self, request):
        encuestas = Encuesta.objects.all()
        serializer = EncuestaSerializer(encuestas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EncuestaDetailView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Encuesta, pk=pk)

    def get(self, request, pk):
        encuesta = self.get_object(pk)
        serializer = EncuestaSerializer(encuesta)
        return Response(serializer.data)

    def put(self, request, pk):
        encuesta = self.get_object(pk)
        serializer = EncuestaSerializer(encuesta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        encuesta = self.get_object(pk)
        encuesta.delete()
        return Response({"msg": f"Encuesta con ID {pk} eliminada"})

    def post(self, request):
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OpcionListCreateView(APIView):

    def get(self, request):
        opciones = Opcion.objects.all()
        serializer = OpcionSerializer(opciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OpcionSerializer(data=request.data)
        if serializer.is_valid():
            encuesta_id = request.data.get('encuesta')
            encuesta = get_object_or_404(Encuesta, pk=encuesta_id)
            serializer.save(encuesta=encuesta)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VotoCreateView(APIView):

    def post(self, request):
        serializer = VotoSerializer(data=request.data)
        if serializer.is_valid():
            opcion_id = request.data.get('opcion')
            opcion = get_object_or_404(Opcion, pk=opcion_id)
            serializer.save(opcion=opcion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
