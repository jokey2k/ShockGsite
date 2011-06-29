from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def shoutbox_recents(context):
    if 'request' not in context:
        raise ImproperlyConfigured('Enable the request context processor!')
    request = context['request']

    from shoutbox.views import recent_entries as recent_entries_view
    return recent_entries_view(request).content

@register.simple_tag(takes_context=True)
def shoutbox_postform(context):
    if 'request' not in context:
        raise ImproperlyConfigured('Enable the request context processor!')
    request = context['request']

    from shoutbox.views import postform as postform_view
    return postform_view(request).content