from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from gameserver.models import Server

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            model=Server,
            context_object_name='serverlist',
            template_name='gameserver/list.html')),
    (r'^(?P<pk>\d+)$',
        DetailView.as_view(
            model=Server,
            context_object_name='entry',
            template_name='gameserver/detail.html')),
)
