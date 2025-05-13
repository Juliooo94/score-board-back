from django.contrib import admin

from score_board.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
