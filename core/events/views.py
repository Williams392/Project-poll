from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework import status

from .models import Events, Ticket, TicketType
from .serializers import EventsSerializer, TicketsSerializer, TicketsTypeSerializer

class EventList(APIView): # Lista de eventos
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
    
    

class EventDetailView(APIView): # VistaDetalleEvento:

    parser_classes = [JSONParser]

    def get(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id) 
        serializer = EventsSerializer(event)
        return Response(serializer.data)

    def put(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id)
        serializer = EventsSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, event_id, format=None):
        event = get_object_or_404(Events, pk=event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
# Nuevo:
class TicketTypesListView(APIView):
    def get(self, request, format=None):
        roles = TicketType.objects.all()
        serializer = TicketsTypeSerializer(roles, many=True)
        return Response(serializer.data)

class TicketListView(APIView):
    def get(self, request, format=None):
        roles = Ticket.objects.all()
        serializer = TicketsSerializer(roles, many=True)
        return Response(serializer.data)
