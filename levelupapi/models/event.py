from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='events_related')
    description = models.CharField(max_length=155)
    date= models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time= models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    organizer= models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='hosted_events')
    attendees= models.ManyToManyField("Gamer", through="EventGamer", related_name='events')
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value