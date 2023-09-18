from rest_framework import serializers
from .models import Events, Ticket, TicketType

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        depth = 1 # nuevo

    '''
    {
      "title": "Feria de reglaos",
      "date": "2023-09-18",
      "hour": "15:30:00",
      "location": "Lugar del evento",
      "description": "Descripción del nuevo evento",
      "organizers": 1  
    }
    '''

class TicketsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'
        depth = 1


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        #fields = ('ticket_type', 'assigned_to', 'code')
        depth = 1 