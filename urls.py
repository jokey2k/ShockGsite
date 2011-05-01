from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.contrib import admin

from sitemap import SitemapForum, SitemapTopic
from forms import RegistrationFormUtfUsername
from djangobb_forum import settings as forum_settings
import polls.urls

# HACK for add default_params with RegistrationFormUtfUsername and backend to registration urlpattern
# Must be changed after django-authopenid #50 (signup-page-does-not-work-whih-django-registration)
# will be fixed
from django_authopenid.urls import urlpatterns as authopenid_urlpatterns
for i, rurl in enumerate(authopenid_urlpatterns):
    if rurl.name == 'registration_register':
        authopenid_urlpatterns[i].default_args.update({'form_class': RegistrationFormUtfUsername})
#                                                  'backend': 'registration.backends.default.DefaultBackend'})
#    elif rurl.name == 'registration_activate':
#                authopenid_urlpatterns[i].default_args = {'backend': 'registration.backends.default.DefaultBackend'}

admin.autodiscover()

sitemaps = {
    'forum': SitemapForum,
    'topic': SitemapTopic,
}

urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),

    # Sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    # Apps
    (r'^board/account/', include(authopenid_urlpatterns)),
    (r'^board/', include('djangobb_forum.urls', namespace='djangobb')),
    (r'^polls/', include('polls.urls')),
    (r'', include('gamesquad.urls'))
)

# PM Extension
if (forum_settings.PM_SUPPORT):
    urlpatterns += patterns('',
        (r'^board/pm/', include('messages.urls')),
   )

if (settings.DEBUG):
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
