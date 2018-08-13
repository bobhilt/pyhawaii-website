import logging

import environ

from .base import *  # noqa


_env = environ.Env()

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

ALLOWED_HOSTS = ('.herokuapp.com')
_additional_hosts = _env('ADDITIONAL_ALLOWED_HOSTS', default='')
if _additional_hosts:
    ALLOWED_HOSTS += _additional_hosts.split(',')
