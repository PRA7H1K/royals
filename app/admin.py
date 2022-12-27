from django.contrib import admin
from .models import StaffRoster, SoccerRoster, BasketballRoster, Injuries, Transactions, Schedule

admin.site.register(StaffRoster)
admin.site.register(SoccerRoster)
admin.site.register(BasketballRoster)
admin.site.register(Injuries)
admin.site.register(Transactions)
admin.site.register(Schedule)
