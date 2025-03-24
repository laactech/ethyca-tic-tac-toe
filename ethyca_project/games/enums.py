from django.db import models


class GameTypeChoices(models.TextChoices):
    TIC_TAC_TOE = "tic_tac_toe", "Tic Tac Toe"
