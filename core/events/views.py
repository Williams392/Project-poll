from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404

from .models import Events
from .serializers import EventsSerializer

# id:
class EventDetailView(APIView): 

    parser_classes = [JSONParser]

    def get(self, request, format=None):
        queryset = Events.objects.all()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    # para crear un nuevo:
    def post(self, request, format=None):
        serializer = EventsSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EventList(APIView):
    parser_classes = [JSONParser]

    def get(self, request, format=None):
        queryset = Events.objects.all()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)