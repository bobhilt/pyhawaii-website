import os


#
# ALL SETTINGS IN THIS FILE SHOULD BE DEFINED DIRECTLY
#

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
PROJECT_ROOT = os.path.dirname(BASE_DIR)


#
# core django
#

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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


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


#
# misc
#

INSTALLING_FROM_FIXTURES = False


#
# fin
#
