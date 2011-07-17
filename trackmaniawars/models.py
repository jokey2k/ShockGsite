import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from gamesquad.models import Squad

from trackmaniawars import settings as trackmaniawars_settings
from specialfields import FramedImageField

choices = [
    _('Team Rounds 2on2'),
    _('Team Rounds 3on3'),
    _('Team Rounds 4on4'),
    _('Team Rounds 5on5'),
    _('Time Attack 2on2'),
    _('Time Attack 3on3'),
    _('Time Attack 4on4'),
    _('Time Attack 5on5')
]
WARMODE_CHOICES = [(x, x) for x in choices]
del choices

WARSTATUS_CHOICES = [
    (1, _('Incomplete')),
    (2, _('Planned')),
    (3, _('Running')),
    (4, _('Finished')),
    (5, _('Aborted')),
    (6, _('Cancelled'))
]

TMXNATION_CHOICES = [
    ('nations', _('Nations')),
    ('tmnforever', _('Nations Forever')),
    ('united', _('United'))
]

class War(models.Model):
    """Clanwar"""
    
    team = models.ForeignKey(Squad)
    opponent = models.CharField(_('Opponent'), max_length=100)
    opponenttag = models.CharField(_('Opponent Clantag'), max_length=10)
    homepage = models.URLField(_('Homepage'), blank=True, null=True, verify_exists=True)
    contact = models.CharField(_('Contact'), max_length=200)
    datetime = models.DateTimeField(_('Date'), default=datetime.datetime.now)
    mode = models.CharField(_('War Mode'), max_length=100, choices=WARMODE_CHOICES)
    server = models.CharField(_('Server'), blank=True, null=True, max_length=100)
    orgamember = models.ForeignKey(User)
    mapsperteam = models.IntegerField(_('Maps per team'))
    notes = models.TextField(_('Notes'), blank=True, null=True)
    our_points = models.IntegerField(_('Our Points'), blank=True, null=True)
    opponent_points = models.IntegerField(_('Opponent Points'), blank=True, null=True)
    resultcomment = models.TextField(_('Resultcomment'), blank=True)
    status = models.IntegerField(_('Status'), blank=True, choices=WARSTATUS_CHOICES)

    class Meta:
        verbose_name = "War"

    def __unicode__(self):
        return u"War against %s" % self.opponent

    def warstatus(self):
        """loss, win or even, untranslated by intentio so it can be used for pictures"""

        if self.status == 3:
            return u"running" 
        elif self.status != 4:
            return u""

        if self.our_points < self.opponent_points:
            return u"loss"
        elif self.our_points > self.opponent_points:
            return u"win"
        else:
            return u"equal"

    def points(self):
        if self.status == 4:
            return u"%i : %i" % (self.our_points, self.opponent_points)
        else:
            return u"-- : --"


class WarMap(models.Model):
    """A map for a war"""
    
    war = models.ForeignKey(War)
    name = models.CharField(_('Mapname'), max_length=100)
    author = models.CharField(_('Author'), blank=True, null=True, max_length=50)
    authortime = models.CharField(_('Author time'), blank=True, null=True, max_length=30)
    tmxid = models.IntegerField(_('TMX ID'), blank=True, null=True)
    tmxnation = models.CharField(_('TMX Nation'), blank=True, null=True, max_length=10, choices=TMXNATION_CHOICES)
    our_points = models.IntegerField(_('Our Points'), blank=True, null=True)
    opponent_points = models.IntegerField(_('Opponent Points'), blank=True, null=True)
    mapfile = models.FileField(_('Map File'), blank=True, upload_to=trackmaniawars_settings.TRACK_UPLOAD_TO)
    thumb = FramedImageField(_('Map Thumbnail'), blank=True, default=trackmaniawars_settings.THUMBS_UPLOAD_TO+'/nopic.png', upload_to=trackmaniawars_settings.THUMBS_UPLOAD_TO, width=trackmaniawars_settings.IMG_WIDTH, height=trackmaniawars_settings.IMG_HEIGHT)

    class Meta:
        verbose_name="War Map"
    
    class Admin:
        list_display = ('war', 'name', 'author', 'map_uploaded')
        search_fields = ('name', 'author')

    def __unicode__(self):
        return u"WarMap %s" % self.name

    def map_uploaded(self):
        return self.mapfile != ''
    map_uploaded.short_description = _('Map uploaded already?')
    map_uploaded.boolean = True


class FightUs(models.Model):
    """Request for a war"""

    team = models.ForeignKey(Squad)
    opponent = models.CharField(_('Opponent'), max_length=100)
    opponenttag = models.CharField(_('Opponent Clantag'), max_length=10)
    homepage = models.URLField(_('Homepage'), blank=True, null=True, verify_exists=True)
    contact = models.CharField(_('Contact'), max_length=200)
    datetime = models.DateTimeField(_('Date'), default=datetime.datetime.now)
    mode = models.CharField(_('Warmode'), max_length=100, choices=WARMODE_CHOICES)
    server = models.CharField(_('Server'), blank=True, null=True, max_length=100)
    mapsperteam = models.IntegerField(_('Maps per team'))
    notes = models.TextField(_('Notes'), blank=True, null=True)

    class Meta:
        verbose_name = "Fight Us"
        verbose_name_plural = "Fight Us"

    class Admin:
        list_display = ('opponent', 'datetime')
        search_fields = ('opponent', 'opponenttag', 'homepage', 'contact', 'server')

    def __unicode__(self):
        return u"FightUs against %s" % self.opponent
