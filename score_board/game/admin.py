from django.contrib import admin

from score_board.game.models.category import Category
from score_board.game.models.game import Game
from score_board.game.models.mechanic import Mechanic


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Mechanic)
class MechanicAdmin(admin.ModelAdmin):
    pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
