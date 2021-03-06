# -*- coding: utf-8 -*-
import os.path
import sys
import re

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Markus Ullmann', 'mail@markus-ullmann.de'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'France'),
    ('lt', 'Lithuanian'),
    ('pl', 'Polish'),
    ('ru', 'Russian'),
    ('zh_CN', 'Chinese'),
    ('de', 'German'),
    ('vi', 'Vietnamese'),
    ('it', 'Italian'),
    ('cs', 'Czech'),
    ('ca', 'Catalan'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = "/media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            import string
            symbols = ''.join((string.lowercase, string.digits, string.punctuation ))
            SECRET_KEY = ''.join([choice(symbols) for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'djangobb_forum.middleware.LastLoginMiddleware',
    'djangobb_forum.middleware.UsersOnline',
)

INTERNAL_IPS = ('127.0.0.1')
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'registration',
    'djangobb_forum',
    'haystack',
    'django_authopenid',
    'polls',
    'gamesquad',
    'news',
    'shoutbox',
    'frontpage',
    'widget_tweaks',
    'ajaxcomments',
    'memberlist',
    'gameserver',
    'trackmaniawars'
)

try:
    import mailer
    INSTALLED_APPS += ('mailer',)
    EMAIL_BACKEND = "mailer.backend.DbBackend"
except ImportError:
    pass

try:
    import south
    INSTALLED_APPS += ('south',)
    SOUTH_TESTS_MIGRATE = False
except ImportError:
    pass

FORCE_SCRIPT_NAME = ''

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django_authopenid.context_processors.authopenid',
    'djangobb_forum.context_processors.forum_settings',
    'frontpage.context_processors.frontpage_loginform',
)

# Haystack settings
HAYSTACK_CONNECTIONS = {
	'default': {
	    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
	    'PATH': os.path.join(PROJECT_ROOT, 'djangobb_index'),
		'STORAGE': 'file',
	    'POST_LIMIT': 128 * 1024 * 1024,
	    'INCLUDE_SPELLING': True,
	    'BATCH_SIZE': 100,
	},
}

# Account settings
ACCOUNT_ACTIVATION_DAYS = 10
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/signin/'

#Cache settings
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

DJANGOBB_PM_SUPPORT = False
DJANGOBB_LOFI_SUPPORT = False

USE_DEBUGBAR = False

SIMPLE_REGEX = r'shock(g|G)'

try:
    from local_settings import *
except ImportError:
    pass

if USE_DEBUGBAR:
	INSTALLED_APPS += ('debug_toolbar',)
	MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
	DEBUG_TOOLBAR_CONFIG = {
    	'INTERCEPT_REDIRECTS': True,
    	'HIDE_DJANGO_SQL': False,
	}

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
