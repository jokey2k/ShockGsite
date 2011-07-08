from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from trackmaniawars.models import War, WarMap, FightUs

class WarMapInlineAdmin(admin.TabularInline):
    model = WarMap


class WarAdmin(admin.ModelAdmin):
    list_display = ('team', 'opponent', 'datetime', 'named_mode', 'status')
    search_fields = ('opponent', 'opponenttag', 'homepage', 'contact', 'server')
    model = War
    inlines = [WarMapInlineAdmin]

    def named_mode(self, model):
        return model.get_mode_display()
    named_mode.short_description = _("War Mode")


admin.site.register(War, WarAdmin)
admin.site.register(WarMap)
admin.site.register(FightUs)