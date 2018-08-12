import logging
import os
import sys

from .base import *  # noqa


DEBUG = bool(os.environ.get('DEBUG', True))
SECRET_KEY = os.environ.get('SECRET_KEY', 'abcdefghijklmnopqrstuvwxyz')
TIME_ZONE = os.environ.get('TIME_ZONE', 'US/Hawaii')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite'),  # noqa
    }
}

FIXTURE_DIRS = ('fixtures',)
INSTALLING_FROM_FIXTURES = len(sys.argv) > 1 and sys.argv[1] == 'loaddata'

TESTING = sys.argv[1] == 'test'
if TESTING:
    logging.disable(logging.CRITICAL)
