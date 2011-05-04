import datetime

from django.db import models

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User


class NewsItem(models.Model):
    """One Newsitem"""

    title = models.CharField(max_length=250)
    intro = models.TextField(blank=True)
    text = models.TextField()
    rendered_text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User)
    published = models.BooleanField(default=True)
    visible_from = models.DateTimeField(blank=True, null=True)
    visible_until = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    updated_author = models.ForeignKey(User, related_name='+')

    class Meta:
        ordering = ['updated']

    def is_visible(self):
        """will the current item be visible?"""

        if not self.published:
            return False

        now = datetime.datetime.now()
        if self.visible_from and self.visible_until:
            return self.visible_from <= now and now <= self.visible_until

        if self.visible_from:
            return self.visible_from <= now

        if self.visible_until:
            return now <= self.visible_until

        return True
    is_visible.short_description = 'Item visible?'
    is_visible.boolean = True

