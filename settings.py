"""=============================================================================
    Settings.py
    ------------
    Handle django settings.  Imports from settings_config.py, which contains 
    local server specific settings
============================================================================="""
import os
import sys
import settings_config

"""--------------------------------------------------------------------------
    Enviornment Specific Settings
-----------------------------------------------------------------------------"""
#Debug settings.  Should never be set to True in production or staging
DEBUG = settings_config.DEBUG
HIDDEN_SETTINGS = True 
TEMPLATE_DEBUG = DEBUG

ENVIRONMENT_TYPES = ['dev', 'production']
SITE_ENVIRONMENT = settings_config.SITE_ENVIRONMENT

#Double check that debug is always false if in production
#if SITE_ENVIRONMENT == ENVIRONMENT_TYPES[1]:
#    DEBUG = False

#Path Of alisenblog folder
#------------
ROOT_PATH = os.path.realpath(os.path.dirname(__file__))

#APACHE URL - Used for urls.py prefix.  Usually will be ''
try:
    URL_PREFIX = settings_config.URL_PREFIX
except AttributeError:
    URL_PREFIX = ''

"""--------------------------------------------------------------------------
    Cache Settings
-----------------------------------------------------------------------------"""
try:
    FORCE_DUMMY_CACHE = settings_config.FORCE_DUMMY_CACHE
except:
    FORCE_DUMMY_CACHE = False

try:
    FORCE_MEMCACHED = settings_config.FORCE_MEMCACHED
except:
    FORCE_MEMCACHED = False

if (SITE_ENVIRONMENT == 'dev' and FORCE_MEMCACHED is False) \
    or (FORCE_DUMMY_CACHE is True):
    CACHE_BACKEND = 'dummy://'
elif SITE_ENVIRONMENT == 'production':
    CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#Overwrite check, just in case
if FORCE_MEMCACHED is True:
    CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

try:
    CACHE_MIDDLEWARE_SECONDS = settings_config.CACHE_MIDDLEWARE_SECONDS 
except AttributeError:
    CACHE_MIDDLEWARE_SECONDS = 60 * 30 * 3

CACHE_MIDDLEWARE_KEY_PREFIX = 'alisenblog'

"""--------------------------------------------------------------------------
    
    Django Database Settings

-----------------------------------------------------------------------------"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'alisen.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

try:
    ADMINS =  settings_config.ADMINS
except AttributeError:
    ADMINS = ()

MANAGERS = ADMINS

"""--------------------------------------------------------------------------
    
    Email Settings

-----------------------------------------------------------------------------"""
#Email Settings
EMAIL_HOST = settings_config.EMAIL_HOST
EMAIL_HOST_USER = settings_config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = settings_config.EMAIL_HOST_PASSWORD
EMAIL_PORT = settings_config.EMAIL_PORT
EMAIL_USE_TLS = settings_config.EMAIL_USE_TLS


"""--------------------------------------------------------------------------
    
    Media Settings 

-----------------------------------------------------------------------------"""
MEDIA_URL = getattr(settings_config, 'MEDIA_URL', '')

"""--------------------------------------------------------------------------
    
    Other Django Settings

-----------------------------------------------------------------------------"""
#Session Age, in seconds
try:
    SESSION_COOKIE_AGE = settings_config.SESSION_COOKIE_AGE
except AttributeError:
    SESSION_COOKIE_AGE = 18000
try:
    SITE_ID = settings_config.SITE_ID
except AttributeError:
    SITE_ID = 1

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'data/www')
MEDIA_URL = 'http://alisenpaige.net/static/alisen/'
ADMIN_MEDIA_PREFIX ='http://alisenpaige.net/static/alisen/'
#ADMIN_MEDIA_PREFIX ='/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q1=sc-b8hqk6^8mhb6wpo8nfo#er3c!@g)2@blz6cl(23*qc8&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'dojango.context_processors.config',
#)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)


MIDDLEWARE_CLASSES = (
    #CACHING
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',

    #OTHER
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #CACHING
    'django.middleware.cache.FetchFromCacheMiddleware',
)

#Login redirect urls
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

#Location of urls.py
ROOT_URLCONF = 'alisenblog.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "data/templates"),
)

FIXTURE_DIRS = (
    os.path.join(ROOT_PATH, 'data/fixtures/'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'alisenblog.blog',
    'alisenblog.site',
)
