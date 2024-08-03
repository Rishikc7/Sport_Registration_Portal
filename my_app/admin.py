from django.contrib import admin

# Register your models here.

from my_app.models import VolleyModel
from my_app.models import CricketModel
from my_app.models import FootballModel
from my_app.models import BasketballModel
from my_app.models import HockeyModel
from my_app.models import KabaddiModel, RegistrationModel,CollegeModel,BadmintonModel,TabletennisModel

admin.site.register(VolleyModel)
admin.site.register(CricketModel)
admin.site.register(FootballModel)
admin.site.register(BasketballModel)
admin.site.register(HockeyModel)
admin.site.register(KabaddiModel)
admin.site.register(RegistrationModel)
admin.site.register(CollegeModel)
admin.site.register(BadmintonModel)
admin.site.register(TabletennisModel)
