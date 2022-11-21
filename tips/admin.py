from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Tip, Round, Team, Match, Season


class TipAdmin(admin.ModelAdmin):
    model = Tip
    list_display = ('round', 'team')


admin.site.register(Tip, TipAdmin)
admin.site.register(Round)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Season)

