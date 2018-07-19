from djangae.settings_base import *  # noqa

import logging
import os
import sys

import djangae.environment

#
# settings that are defined differently between dev and production
#

if djangae.environment.is_production_environment():

    DEBUG = False

    import app_engine_only as overrides
    SECRET_KEY = overrides.SECRET_KEY

    TIME_ZONE = 'UTC'

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    ALLOWED_HOSTS = ()

    _extra_cors_origins = ()

    logging.disable(logging.DEBUG)

    INSTALLING_FROM_FIXTURES = False

else:

    DEBUG = True

    SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz'

    TIME_ZONE = 'UTC'

    DJANGAE_ADDITIONAL_MODULES = []

    _local_ports = [8000 + i for i in range(len(DJANGAE_ADDITIONAL_MODULES) + 1)] + [9000]
    _extra_cors_origins = [
        '{domain}:{port}'.format(domain=domain, port=port)
        for domain in ['localhost', 'localhost.com', '127.0.0.1']
        for port in _local_ports
    ]

    TESTING = sys.argv[1] == 'test'
    if TESTING:
        logging.disable(logging.CRITICAL)

    FIXTURE_DIRS = ["fixtures"]
    INSTALLING_FROM_FIXTURES = len(sys.argv) > 1 and sys.argv[1] == 'loaddata'


#
# ALL SETTINGS AFTER THIS POINT SHOULD BE DEFINED DIRECTLY
#

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#
# core django
#

DATABASES = {
    'default': {
        'ENGINE': 'djangae.db.backends.appengine',
    }
}

INSTALLED_APPS = (
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

    'accounts',

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
# django-cors-headers
#

CORS_ORIGIN_WHITELIST = [] + _extra_cors_origins

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'x-app-id',
)


#
# django-session-csrf
#

ANON_ALWAYS = True


#
#
#
