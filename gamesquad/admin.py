from gamesquad.models import Game, Level, Squad, Squadmember
from django.contrib import admin
from django.contrib.auth.models import User


class SquadmemberInlineAdmin(admin.TabularInline):
    model = Squadmember
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Limit user choice for new squad members to active users only"""

        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_active=True).order_by('username')
        return super(SquadmemberInlineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class SquadAdmin(admin.ModelAdmin):
    list_display = ('name','game')
    model = Squad
    inlines = [SquadmemberInlineAdmin]
    search_fields = ['name']


class LevelAdmin(admin.ModelAdmin):
    list_display = ('position', 'name')
    search_fields = ['name']


admin.site.register(Game)
admin.site.register(Squad, SquadAdmin)
admin.site.register(Level, LevelAdmin)
