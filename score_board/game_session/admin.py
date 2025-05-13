from django.contrib import admin

from score_board.game_session.models.game_session import GameSession
from score_board.game_session.models.player import Player
from score_board.game_session.models.result import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    pass
