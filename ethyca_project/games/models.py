from django.db import models

from ethyca_project.core.mixins import BaseModel
from ethyca_project.games.enums import GameTypeChoices


class Game(BaseModel):
    game_type = models.CharField(choices=GameTypeChoices.choices, max_length=50)


class GameMove(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_state = models.JSONField()
