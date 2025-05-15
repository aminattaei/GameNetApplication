from django.contrib import admin
from .models import (
    Game,
    OperatingSystem,
    GameNews,
    TeamMember,
    Tournament,
    UpcomingGame,
)


class OperatingSystemInline(admin.TabularInline):
    model = OperatingSystem
    extra = 0



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "launch_date",
        "price",
        "rating",
        "stars",
        "download_link",
        "description",
    )
    list_filter = ["launch_date", "rating", "price"]
    inlines = [OperatingSystemInline]





admin.site.register(GameNews)
admin.site.register(TeamMember)
admin.site.register(Tournament)
admin.site.register(UpcomingGame)
