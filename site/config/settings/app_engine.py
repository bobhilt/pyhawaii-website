import logging

import gae_app_settings

from .base import *  # noqa


_env = gae_app_settings.AppSetting.get

logging.disable(logging.DEBUG)


#
# invariants
#

DEBUG = False
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


#
# pulled from environment
#

SECRET_KEY = _env('SECRET_KEY')
TIME_ZONE = _env('TIME_ZONE')

_db_username, _db_password = _env('DATABASE_CREDS').split('|')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'djangodb',
        'USER': _db_username,
        'PASSWORD': _db_password,
    }
}

_additional_hosts = _env('ADDITIONAL_ALLOWED_HOSTS', default='')
ALLOWED_HOSTS = ('.appspot.com',) + _additional_hosts.split(',') if _additional_hosts else ()

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = _env('GOOGLE_OAUTH2_CREDS').split('|')
