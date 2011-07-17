from django.db import models
from django.utils.translation import ugettext_lazy as _

from gameserver import settings as gameserver_settings
from specialfields import FramedImageField

class Server(models.Model):
    """A basic game server"""

    name = models.CharField(_('Servername'), max_length=100)
    playercount = models.IntegerField(_('Player Count'))
    maxplayercount = models.IntegerField(_('Max Player Count'))
    spectatorcount = models.IntegerField(_('Spectator Count'))
    maxspectatorcount = models.IntegerField(_('Max Spectator Count'))
    currentmap = models.CharField(_('Current Map'), blank=True, max_length=100)
    currentmapauthor = models.CharField(_('Current Map Author'), blank=True, max_length=100)
    nextmap = models.CharField(_('Next Map'), blank=True, max_length=100)
    nextmapauthor = models.CharField(_('Next Map Author'), blank=True, max_length=100)
    serverlogin = models.CharField(_('Server Login (for joinlinks)'), max_length=100)
    mode = models.CharField(_('Game Mode'), blank=True, max_length=100)
    status = models.CharField(_('Server Status'), blank=True, max_length=100)
    image = FramedImageField(_('Server / Map Picture'), blank=True, default='', upload_to=gameserver_settings.UPLOAD_TO, width=gameserver_settings.IMG_WIDTH, height=gameserver_settings.IMG_HEIGHT)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Admin:
        list_display = ('name', 'currentmap', 'status', 'updated')
        search_fields = ('name', 'currentmap', 'mapauthor', 'nextmap', 'nextmapauthor')

    def __unicode__(self):
        return u"Gameserver %s" % self.name
        
    
class Player(models.Model):
    """Players on a server"""

    gameserver = models.ForeignKey(Server)
    nickname = models.CharField(max_length=100)
    position = models.IntegerField()
    status = models.CharField(max_length=100)
    
    class Admin:
        list_display = ('gameserver', 'nickname', 'position')
        search_fields = ('nickname',)

    def __unicode__(self):
        return u"Player %s" % self.nickname


class UpdateConfig(models.Model):
    """Configuration data to update a server"""

    gameserver = models.ForeignKey(Server)
    hostname = models.CharField(max_length=100)
    port = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gametype = models.CharField(max_length=100)
    
    class Admin:
        list_display = ('gametype', 'hostname', 'port', 'username')
        search_fields = ('hostname', 'port', 'username')
    
    def __unicode__(self):
        return u"UpdateConfig %s" % self.gameserver.name
        