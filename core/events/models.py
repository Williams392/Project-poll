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


    def __str__(self):
        return self.title
    
class Presents (models.Model):
    id_profile = models.ForeignKey (Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey (Events, on_delete=models.PROTECT, null= False)
    
    def __str__(self):
        return self.id_profile 
    
class Interested (models.Model):
    id_profile = models.ForeignKey (Profile, on_delete=models.PROTECT, null= False)
    id_event = models.ForeignKey (Events, on_delete=models.PROTECT, null= False)
    
    def __str__(self):
        return self.id_profile
     
     