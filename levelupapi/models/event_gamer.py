from django.db import models
from django.contrib.auth.models import User


class EventGamer(models.Model):
    # how do I state the best way the related name?
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='events_assisting')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='confirmed_gamer')

