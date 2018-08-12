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
