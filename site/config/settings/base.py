import os

from django.core.exceptions import ImproperlyConfigured
import environ


#
# ALL SETTINGS IN THIS FILE SHOULD BE DEFINED DIRECTLY
#

SETTINGS_PATH = environ.Path(__file__) - 1
BASE_PATH = SETTINGS_PATH - 2
PROJECT_ROOT = BASE_PATH - 1
APPS_PATH = BASE_PATH('apps')


#
# environment variables and overrides
#

_envfile_path = os.environ.get('DJANGO_ENVFILE_PATH', BASE_PATH('.env'))
if os.path.isfile(_envfile_path):
    environ.Env.read_env(_envfile_path)

_env = environ.Env()

#
# database
#

try:
    DATABASES = {'default': _env.db('DATABASE_URL')}
except ImproperlyConfigured:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': PROJECT_ROOT('db.sqlite')}}  # noqa


#
# core django
#

DEBUG = _env.bool('DEBUG', default=True)
SECRET_KEY = _env('SECRET_KEY', default='abcdefghijklmnopqrstuvwxyz')

INSTALLED_APPS = (
    # before django.contrib.admin
    'djangocms_admin_style',

    # core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # before cms
    'apps.accounts',

    # cms
    'cms',
    'menus',
    'sekizai',
    'treebeard',

    # third party apps
    'social_django',

    # project apps
    # ...

    # this must be the very last app
    'config.apps.Config',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            BASE_PATH.path('templates'),
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
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ),
        },
    },
)

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

ROOT_URLCONF = 'config.urls'
LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_PATH('collected-static')

TIME_ZONE = _env('TIME_ZONE', default='US/Hawaii')

ALLOWED_HOSTS = ('*',)


#
# using Google Cloud Storage for files
#

# DEFAULT_FILE_STORAGE = 'djangae.storage.CloudStorage'
# CLOUD_STORAGE_BUCKET = None  # replace with name of bucket to use for files
# BUCKET_KEY = CLOUD_STORAGE_BUCKET
# BUCKET_ACL = 'project-private'


#
# django-cms
#

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)


#
# social-auth-django
#

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ('email', 'first_name', 'last_name')
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
) + AUTHENTICATION_BACKENDS
try:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = _env('GOOGLE_OAUTH2_CREDS').split('|')
except ImproperlyConfigured:
    pass


#
# misc
#

INSTALLING_FROM_FIXTURES = False


#
# fin
#
