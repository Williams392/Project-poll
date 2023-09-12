# Estructura de la app movil Events:

from django.db import models
from fundamentals.models import Club
from authentication.models import Profile

class Events(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    hour = models.TimeField(null=False, blank=False)
    location = models.CharField(max_length=150, null=False, blank=False)
    event_type = models.CharField(max_length=200, null=False, blank=False)
    contribution = models.CharField(max_length=200, null=False, blank=False) 
    description = models.TextField(null=False, blank=False)
    
    organizers = models.ForeignKey(Club, on_delete=models.CASCADE, null=True, blank=True)
    present = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True) 

    # Para no mostrar <Events object> si no mostrará el valor del campo title.
    def __str__(self):
        return self.title
    
# Asistentes: 
class Presents (models.Model):
    id_profile = models.ForeignKey (Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey (Events, on_delete=models.PROTECT, null= False)  
    attending = models.BooleanField(default=False)  # (asistiendo)si el usuario asistirá al evento 
    
    def __str__(self):
        return self.id_profile 
    
# Interesados:
class Interested (models.Model):
    id_profile = models.ForeignKey (Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey (Events, on_delete=models.PROTECT, null= False)
    interested = models.BooleanField(default=False)  # (interesado)si el usuario está interesado en el evento

    def __str__(self): # Nombre del Perfil - Título del Evento
        return f"{self.profile} - {self.event}"
    
    def __str__(self):
        return self.id_profile
    


# comando -> [python manage.py makemigrations}
# comando -> [python manage.py migrate}
# comando -> [python manage.py runserver}
     
     