from django.contrib import admin
from .models import StaffRoster, SoccerRoster, BasketballRoster, Injuries, Schedule, Player

admin.site.register(StaffRoster)
admin.site.register(SoccerRoster)
admin.site.register(BasketballRoster)
admin.site.register(Injuries)
admin.site.register(Schedule)
admin.site.register(Player)