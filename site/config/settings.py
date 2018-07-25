from djangae.settings_base import *  # noqa

import logging
import os
import sys

import djangae.environment
import gae_app_settings


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#
# settings that are defined differently between dev and production
#

if djangae.environment.is_production_environment():

    _env = gae_app_settings.AppSetting.get

    DEBUG = False

    SECRET_KEY = _env('SECRET_KEY')
    TIME_ZONE = _env('TIME_ZONE')
    SITE_ID = _env('DEFAULT_SITE_ID')
    ALLOWED_HOSTS = ('.appspot.com',)

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    logging.disable(logging.DEBUG)

    INSTALLING_FROM_FIXTURES = False

else:

    DEBUG = bool(os.environ.get('DEBUG', True))
    SECRET_KEY = os.environ.get('SECRET_KEY', 'abcdefghijklmnopqrstuvwxyz')
    TIME_ZONE = os.environ.get('TIME_ZONE', 'US/Hawaii')
    SITE_ID = 1

    TESTING = sys.argv[1] == 'test'
    if TESTING:
        logging.disable(logging.CRITICAL)

    FIXTURE_DIRS = ('fixtures',)
    INSTALLING_FROM_FIXTURES = len(sys.argv) > 1 and sys.argv[1] == 'loaddata'


#
# ALL SETTINGS AFTER THIS POINT SHOULD BE DEFINED DIRECTLY
#

#
# core django
#

DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine',
    }
}

INSTALLED_APPS = (

    # core apps
    'djangae',

    'django.contrib.admin',
    'django.contrib.auth',

    'djangae.contrib.gauth_datastore',

    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'djangae.contrib.contenttypes',
    'djangae.contrib.security',

    'django.contrib.sites',

    # project apps
    'accounts',

    # third party apps
    'social_django',

    # this must be the very last app
    'config.apps.Config',
)

MIDDLEWARE_CLASSES = (
    'djangae.contrib.security.middleware.AppEngineSecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'djangae.contrib.gauth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'session_csrf.CsrfMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'djangae.contrib.gauth_datastore.backends.AppEngineUserAPIBackend',
)

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            os.path.join(BASE_DIR, 'templates'),
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'session_csrf.context_processor',
            ),
        },
    },
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ROOT_URLCONF = 'config.urls'

LOGIN_REDIRECT_URL = '/'

APPEND_SLASH = True


#
# using google accounts for users
#

AUTH_USER_MODEL = 'accounts.User'
DJANGAE_CREATE_UNKNOWN_USER = False


#
# using Google Cloud Storage for files
#

DEFAULT_FILE_STORAGE = 'djangae.storage.CloudStorage'
CLOUD_STORAGE_BUCKET = None  # replace with name of bucket to use for files
BUCKET_KEY = CLOUD_STORAGE_BUCKET
BUCKET_ACL = 'project-private'


#
# django-session-csrf
#

ANON_ALWAYS = True


#
# using social auth django for user authentication
#

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ('email', 'first_name', 'last_name')
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
) + AUTHENTICATION_BACKENDS

if djangae.environment.is_production_environment():
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = _env('GOOGLE_OAUTH2_CREDS').split('|')


#
#
#
