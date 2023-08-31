from django.contrib import admin
from .models import Events, Presents, Interested

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'hour', 'location', 'event_type')
    list_filter = ('date', 'event_type')
    search_fields = ('title', 'location')

class PresentsAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_event')

class InterestedAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'id_event')
    
admin.site.register(Events, EventsAdmin)
admin.site.register(Presents, PresentsAdmin)
admin.site.register(Interested, InterestedAdmin)