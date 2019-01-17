import logging
import sys

from .base import *  # noqa


FIXTURE_DIRS = ('fixtures',)
INSTALLING_FROM_FIXTURES = len(sys.argv) > 1 and sys.argv[1] == 'loaddata'

TESTING = sys.argv[1] == 'test'
if TESTING:
    logging.disable(logging.CRITICAL)
