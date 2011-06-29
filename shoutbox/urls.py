from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from shoutbox.models import ShoutboxEntry

urlpatterns = patterns('',
    (r'^archive/$',
        ListView.as_view(
            queryset=ShoutboxEntry.objects.all(),
            context_object_name='entries',
            template_name='shoutbox/archive.html',
            paginate_by=20,
            ),
            {},
            'shoutbox.archive'),
    (r'^post$', 'shoutbox.views.postform'),
    (r'^recents$', 'shoutbox.views.recent_entries'),
)
