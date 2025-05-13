from django.contrib.auth.models import AbstractUser

from score_board.models import UUIDModel


class User(AbstractUser, UUIDModel):
    pass