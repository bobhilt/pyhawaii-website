from google.appengine.ext import vendor
vendor.add('sitepackages')

import os  # noqa
from django.core.wsgi import get_wsgi_application  # noqa


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.app_engine')
application = get_wsgi_application()
