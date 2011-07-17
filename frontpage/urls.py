from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^$', 'frontpage.views.frontpage'),
    (r'^impressum$', 'frontpage.views.impressum'),
)
