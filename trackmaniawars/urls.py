from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView

from trackmaniawars.models import War

urlpatterns = patterns('',
    (r'^$',
        ListView.as_view(
            model=War,
            context_object_name='warlist',
            paginate_by=20,
            template_name='trackmaniawars/list.html')),
    (r'^(?P<pk>\d+)$',
        DetailView.as_view(
            model=War,
            context_object_name='entry',
            template_name='trackmaniawars/detail.html')),
)
