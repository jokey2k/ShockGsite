from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^$', 'frontpage.views.frontpage'),
)
