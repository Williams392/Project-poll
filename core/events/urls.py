# siempre os nombres adentro del PATH en minuscula:

from django.urls import path
from .views import EventList, EventDetailView, TicketListView, TicketTypesListView, TicketScanView

urlpatterns = [
    path('', EventList.as_view(), name='event-list'), 
    path('<int:event_id>/', EventDetailView.as_view(), name='post-detail-update-delete'),
    path('<int:event_id>/tickets-available/', TicketTypesListView.as_view(), name='tickets-Types'), 
    path('tickets/', TicketListView.as_view(), name='ticket'), 
    path('tickets/scan/', TicketScanView.as_view(), name='ticket-scan')
]

'''
--------------------------------------------
. event-list -> lista de eventos
. ticket-list -> lista de boletos
. ticket-types -> lista de tipos de boletos
. ticket-scan -> escaneo de boletos
. tickets-available ->  tickets-disponibles
--------------------------------------------
'''