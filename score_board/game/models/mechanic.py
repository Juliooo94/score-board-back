from django.db import models
from score_board.models import UUIDModel


class Mechanic(UUIDModel):
    class MechanicChoices(models.TextChoices):
        AREA_CONTROL = "area_control"
        AUCTION = "auction"
        DECK_BUILDING = "deck_building"
        DICE_ROLLING = "dice_rolling"
        HAND_MANAGEMENT = "hand_management"
        MEMORY = "memory"
        SIMULATION = "simulation"
        TILE_LAYING = "tile_laying"
        TRICK_TAKING = "trick"
        WORKER_PLACEMENT = "worker_placement"

    name = models.CharField(choices=MechanicChoices, default=MechanicChoices.DECK_BUILDING)