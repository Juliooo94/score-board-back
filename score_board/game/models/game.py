from django.db import models
from django.contrib.postgres.fields import ArrayField
from score_board.models import UUIDModel

"""
Ideas of field to add later:
- Description
- Playing time (min/max/mean ?)
- publisher (maybe FK)
- published year
"""


class Game(UUIDModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    min_player = models.PositiveIntegerField(null=False, blank=False)
    max_player = models.PositiveIntegerField(null=False, blank=False)
    best_player_count = ArrayField(base_field=models.PositiveIntegerField(), default=list)
    min_age = models.PositiveIntegerField(null=False, blank=False)
    category = models.ManyToManyField(to='Category', related_name='game')
    mechanics = models.ManyToManyField(to='Mechanic', related_name='game')
    image_url = models.CharField(null=True, blank=True)
