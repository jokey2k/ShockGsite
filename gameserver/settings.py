# -*- coding: utf-8 -*-
from django.conf import settings

def get(key, default):
    return getattr(settings, key, default)

UPLOAD_TO = get('GAMESERVER_UPLOAD_TO', 'gameserver/serverimgs')

IMG_WIDTH=get('GAMESERVER_IMG_WIDTH', 194)
IMG_HEIGHT=get('GAMESERVER_IMG_HEIGHT', 144)
