from rest_framework import serializers
from .models import Encuesta, Opcion, Voto

class VotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voto
        fields = '__all__'

class OpcionSerializer(serializers.ModelSerializer):
    votos = VotoSerializer(many=True, read_only=True)

    class Meta:
        model = Opcion
        fields = '__all__'

class EncuestaSerializer(serializers.ModelSerializer):
    opciones = OpcionSerializer(many=True, read_only=True)

    class Meta:
        model = Encuesta
        fields = ('id', 'titulo', 'fecha', 'hora', 'opciones', 'estado', 'fech_creacion', 'fech_edicion')

