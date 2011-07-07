from django.contrib import admin

from trackmaniawars.models import War, WarMap, FightUs

class WarMapInlineAdmin(admin.TabularInline):
    model = WarMap

class WarAdmin(admin.ModelAdmin):
    list_display = ('team', 'opponent', 'datetime')
    search_fields = ('opponent', 'opponenttag', 'homepage', 'contact', 'server')
    model = War
    inlines = [WarMapInlineAdmin]
        
admin.site.register(War, WarAdmin)
admin.site.register(WarMap)
admin.site.register(FightUs)