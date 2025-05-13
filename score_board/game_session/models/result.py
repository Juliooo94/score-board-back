from django.db import models
from score_board.models import UUIDModel


class Result(UUIDModel):
    game_sessionn = models.ForeignKey('GameSession', on_delete=models.CASCADE)
    winner = models.ForeignKey('Player', on_delete=models.CASCADE)