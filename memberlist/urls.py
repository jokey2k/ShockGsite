from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^memberlist$', 'memberlist.views.memberlist'),
)
