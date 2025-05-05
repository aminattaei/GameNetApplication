from django.contrib import admin
from .models import (
    Game,
    OperatingSystem,
    Comment,
    GameNews,
    TeamMember,
    Tournament,
    UpcomingGame,
)





admin.site.register(OperatingSystem)
admin.site.register(Comment)
admin.site.register(GameNews)
admin.site.register(TeamMember)
admin.site.register(Tournament)
admin.site.register(UpcomingGame)
admin.site.register(Game)

