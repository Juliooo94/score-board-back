from django.db import models
from score_board.models import UUIDModel


class Category(UUIDModel):
    class CategoryChoices(models.TextChoices):
        BOARD = "board"
        CARD = "card"
        CREATIVE = "creative"
        COOPERATION = "coop"
        DEXTERITY = "dexterity"
        DICE = "dice"
        INVESTIGATION = "investigation"
        KNOWLEDGE = "knowledge"
        LETTER = "letter"
        LOGIC = "logic"
        MEMORY = "memory"
        NARRATIVE = "narrative"
        STRATEGY = "strategy"
        DECK_BUILDING = "deck_building"
        PARTY = "party"
    name = models.CharField(choices=CategoryChoices, default=CategoryChoices.BOARD)