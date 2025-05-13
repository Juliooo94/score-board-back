from django.db import models
from score_board.models import UUIDModel


class Player(UUIDModel):
    game_session = models.ForeignKey('GameSession', on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True)
    score = models.FloatField(null=True, blank=True)