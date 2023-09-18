from django.urls import path
from .views import EventList, EventDetailView, TicketListView, TicketTypesListView

urlpatterns = [
    # actualizar y borrar:
    path('events/', EventList.as_view(), name='post-list-create'), 
    path('events/<int:event_id>/', EventDetailView.as_view(), name='post-detail-update-delete'),

    # Nuevo:
    #path('events/<int:event_name>/', EventDetailedViewName.as_view(), name='event'),
    path('tickets-Types/', TicketTypesListView.as_view(), name='tickets-Types'), 
    path('tickets/', TicketListView.as_view(), name='ticket'), 
]