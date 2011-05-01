from django.db import models
from djangobb_forum.fields import ExtendedImageField
from djangobb_forum import settings as forum_settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Game(models.Model):
    """A Game"""

    name = models.CharField(_('Name'), max_length=80)
    picture = ExtendedImageField(_('Picture'), blank=True, default='', upload_to=forum_settings.AVATARS_UPLOAD_TO, width=forum_settings.AVATAR_WIDTH, height=forum_settings.AVATAR_HEIGHT)

    class Meta:
        verbose_name = _('Game')
        verbose_name_plural = _('Games')

    def __unicode__(self):
        return self.name


class Level(models.Model):
    """Squadmembership level"""

    name = models.CharField(_('Name'), max_length=80)
    position = models.IntegerField(_('Position'), blank=True, default=0)

    class Meta:
        ordering = ['position']
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')

    def __unicode__(self):
        return self.name


class Squad(models.Model):
    """A Squad"""

    game = models.ForeignKey(Game, related_name='squads', verbose_name=_('Game'))
    name = models.CharField(_('Name'), max_length=80)
    tag = models.CharField(_('Tag'), max_length=20)

    def __unicode__(self):
        return self.name


class Squadmember(models.Model):
    """Squadmembership"""

    user = models.ForeignKey(User, related_name='squadmemberships')
    squad = models.ForeignKey(Squad, related_name='members')
    level =  models.ForeignKey(Level)

    class Meta:
        ordering = ['level', 'user__username']
        unique_together = (("user", "squad"),)

    def __unicode__(self):
        return "%s, %s" % (self.user.username, self.squad.name)
