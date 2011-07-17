from django import template
from django.core.exceptions import ImproperlyConfigured

register = template.Library()

@register.simple_tag(takes_context=True)
def frontpage_statusbox(context):
    if 'request' not in context:
        raise ImproperlyConfigured('Enable the request context processor!')
    request = context['request']

    from frontpage.views import statusbox
    return statusbox(request).content
