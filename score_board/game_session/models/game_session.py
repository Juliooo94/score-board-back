from django.utils import timezone
from django.db import models

from score_board.models import UUIDModel


class GameSession(UUIDModel):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, null=True)
    played_date = models.DateField(default=timezone.now)
