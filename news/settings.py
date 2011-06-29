# -*- coding: utf-8 -*-
from django.conf import settings

def get(key, default):
    return getattr(settings, key, default)

UPLOAD_TO = get('NEWS_UPLOAD_TO', 'news/newsimgs')

BIGIMG_WIDTH=get('NEWS_BIGIMG_WIDTH', 196)
BIGIMG_HEIGHT=get('NEWS_BIGIMG_HEIGHT', 144)

IMG_WIDTH=get('NEWS_IMG_WIDTH', 139)
IMG_HEIGHT=get('NEWS_IMG_HEIGHT', 74)
