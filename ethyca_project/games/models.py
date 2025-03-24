from django.contrib.auth import get_user_model
from django.db import models

from ethyca_project.core.mixins import BaseModel
from ethyca_project.games.enums import GameTypeChoices

User = get_user_model()


class Game(BaseModel):
    game_type = models.CharField(choices=GameTypeChoices.choices, max_length=50)


class GameMove(BaseModel):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game_moves")
    game_state = models.JSONField()
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_moves")

    def clean(self):
        if not isinstance(self.game_state, (list, tuple)):
            raise ValueError("game_state must be a list or tuple")
        if len(self.game_state) != 3:
            raise ValueError("game_state must be of length 3")
        for row in self.game_state:
            if not isinstance(row, (list, tuple)) or len(row) != 3:
                raise ValueError("Each row in game state must be a list or tuple and of length 3")
            if not all(element in {"x", "o", "."} for element in row):
                raise ValueError("Each row in game state must contain either 'x', 'o' or '.'")
