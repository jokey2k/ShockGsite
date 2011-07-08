from django import template
from django.shortcuts import redirect, render

from trackmaniawars.models import War

register = template.Library()

@register.simple_tag(takes_context=True)
def trackmaniawars_upcoming(context):
    """Render upcoming wars, adding None items so we have full length in template in all cases"""
    
    if 'request' not in context:
        raise ImproperlyConfigured('Enable the request context processor!')
    request = context['request']
    
    entries = War.objects.filter(status=2).order_by('datetime')[:3]
    wars = [war for war in entries]
    if len(wars) < 3:
        for war in range(3-len(wars)):
            wars.append(None)

    return render(request, 'trackmaniawars/upcomingwars.html', {'wars':wars}).content

@register.simple_tag(takes_context=True)
def trackmaniawars_past(context):
    """Render past wars, adding None items so we have full length in template in all cases"""

    if 'request' not in context:
        raise ImproperlyConfigured('Enable the request context processor!')
    request = context['request']

    entries = War.objects.filter(status=4).order_by('datetime')[:3]
    wars = [war for war in entries]
    if len(wars) < 3:
        for war in range(3-len(wars)):
            wars.append(None)

    return render(request, 'trackmaniawars/pastwars.html', {'wars':wars}).content
