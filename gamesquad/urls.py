from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from gamesquad.models import Game, Squad

urlpatterns = patterns('',
    (r'^games/$',
        ListView.as_view(
            model=Game,
            context_object_name='gamelist',
            template_name='gamesquad/game/list.html')),
    (r'^games/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Game,
            template_name='gamesquad/game/detail.html')),
    (r'^squads/$',
        ListView.as_view(
            model=Squad,
            context_object_name='squadlist',
            template_name='gamesquad/squad/list.html')),
    (r'^squads/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Game,
            template_name='gamesquad/squad/detail.html')),
)
