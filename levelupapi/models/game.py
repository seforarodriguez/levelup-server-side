from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='chosen_gametype')
    title = models.CharField(max_length=30)
    maker = models.CharField(max_length=20)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='game_creator')
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    
    