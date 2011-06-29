from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404

from news.models import NewsItem

# Create your views here.

def recent_entries(request, entrycount=4, template='news/recents.html', offset=None):
    """Render a set of recent entries"""

    if offset is not None:
        entries = NewsItem.objects.all()[offset:offset+entrycount]
    else:
        entries = NewsItem.objects.all()[:entrycount]

    return render(request, template, {'entries':entries})
