# -*- coding: utf-8 -*-
from django.conf import settings

def get(key, default):
    return getattr(settings, key, default)

TRACK_UPLOAD_TO = get('TRACKMANIAWARS_TRACK_UPLOAD_TO', 'tracknamiawars/tracks')

THUMBS_UPLOAD_TO = get('TRACKMANIAWARS_THUMBS_UPLOAD_TO', 'tracknamiawars/thumbs')
IMG_WIDTH=get('GAMESERVER_IMG_WIDTH', 194)
IMG_HEIGHT=get('GAMESERVER_IMG_HEIGHT', 144)
