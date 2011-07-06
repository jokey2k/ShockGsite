from django.contrib import admin

from gameserver.models import Server, Player, UpdateConfig

admin.site.register(Server)
admin.site.register(Player)
admin.site.register(UpdateConfig)
