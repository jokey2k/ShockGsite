from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView
from news.models import NewsItem

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            queryset=NewsItem.objects.all(),
            context_object_name='newsitems',
            template_name='news/index.html'),
            {},
            'news.list'),
    (r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=NewsItem,
            template_name='news/detail.html',
            context_object_name='entry'),
            {},
            'news.detail'),
)
