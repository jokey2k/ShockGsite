from shoutbox.models import ShoutboxEntry
from django.contrib import admin

class ShoutboxEntryAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created', 'text')
    list_filter = ['created']
    search_fields = ['text', 'author_name']
    date_hierarchy = 'created'

admin.site.register(ShoutboxEntry, ShoutboxEntryAdmin)