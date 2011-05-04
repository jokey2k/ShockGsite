# -*- coding: utf-8 -*-
from django.contrib import admin
#from django.contrib.admin import BooleanFieldListFilter
from django.contrib.auth.models import User

from news.models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'intro', 'text', 'author']}),
        ('Visibility information', {'fields': ['published', 'visible_from', 'visible_until']}),
    ]
    list_display = ('title', 'author', 'is_visible', 'visible_from', 'visible_until')
    list_filter = ['updated', 'is_visible']
    search_fields = ['title', 'intro', 'text']
    date_hierarchy = 'updated'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Limit user choice for new squad members to active users only"""
        print db_field.name
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(is_active=True).order_by('username')
        return super(NewsItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        obj.updated_author = request.user
        obj.save()


admin.site.register(NewsItem, NewsItemAdmin)