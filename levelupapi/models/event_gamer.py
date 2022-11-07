from django.db import models
from django.contrib.auth.models import User


class EventGamer(models.Model):
    # how to I state the best way the related name?
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE, related_name='confirmed_gamer')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='assigned_event')

