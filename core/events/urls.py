from django.urls import path
from .views import EventList, EventDetailView

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'), 

    path('events/<int:event_id>/', EventDetailView.as_view(), name='event-detail'),
]