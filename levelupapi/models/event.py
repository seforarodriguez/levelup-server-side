from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='selected_game')
    description = models.CharField(max_length=155)
    date= models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    time= models.TimeField(null=True, blank=True, auto_now=False, auto_now_add=False)
    organizer= models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='game_organizer')
    