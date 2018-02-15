"""
Django settings for coss project.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import sys

from decouple import Csv, config
from dj_database_url import parse as db_url
from django_jinja.builtins import DEFAULT_EXTENSIONS
from unipath import Path


#######################
# Environment Variables
#######################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = Path(__file__).parent.parent
BASE_DIR = Path(__file__).parent.parent.parent
STATIC_ROOT = Path('static').resolve()
STATIC_URL = config('STATIC_URL', default='/static/')
MEDIA_ROOT = Path('media').resolve()
ROOT_URLCONF = 'coss.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')
TIME_ZONE = config('TIME_ZONE', default='UTC')
USE_I18N = config('USE_I18N', default=True, cast=bool)
USE_L10N = config('USE_L10N', default=True, cast=bool)
USE_TZ = config('USE_TZ', default=True, cast=bool)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# S3 storages
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
AWS_LOCATION = config('AWS_LOCATION', default='cms')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN',
                              default='{0}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME))

MEDIA_URL = config('MEDIA_URL', default='https://{0}/'.format(AWS_S3_CUSTOM_DOMAIN))
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=not DEBUG, cast=bool)


# This is needed to get a CRSF token in /admin
ANON_ALWAYS = config('ANON_ALWAYS', default=True, cast=bool)

# A boolean that specifies whether to use the X-Forwarded-Host header in
# preference to the Host header. This should only be enabled if a proxy which
# sets this header is in use.
USE_X_FORWARDED_HOST = config('USE_X_FORWARDED_HOST', default=False, cast=bool)

# When DEBUG is True, allow HTTP traffic, otherwise, never allow HTTP traffic.
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=not DEBUG, cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default='31536000', cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False, cast=bool)
SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', default=True, cast=bool)
SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = config('DEBUG', default=False, cast=bool)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    # Project specific apps
    'coss.base',
    'coss.global_components',
    'coss.demo',

    # Third party apps
    'django_jinja',
    'storages',

    # Wagtail
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'modelcluster',
    'taggit',

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)


MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_csrf.CsrfMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',

    # Wagtail middleware
    'wagtail.wagtailcore.middleware.SiteMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'match_extension': '.jinja',
            'newstyle_gettext': True,
            'context_processors': [
                'session_csrf.context_processor',
                'coss.base.context_processors.settings',
                'coss.base.context_processors.i18n',
            ],
            'extensions': DEFAULT_EXTENSIONS + [
                'wagtail.wagtailcore.jinja2tags.core',
                'wagtail.wagtailadmin.jinja2tags.userbar',
                'wagtail.wagtailimages.jinja2tags.images'
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'session_csrf.context_processor',
            ],
        }
    },
]

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': config('DATABASE_URL', cast=db_url)
}

WSGI_APPLICATION = 'coss.wsgi.application'

###############
# Configuration
###############

# Django-CSP
CSP_DEFAULT_SRC = (
    "'self'",
)
CSP_FONT_SRC = (
    "'self'",
)
CSP_IMG_SRC = (
    "'self'",
)
CSP_SCRIPT_SRC = (
    "'self'",
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
)

CSP_WORKER_SRC = (
    "'self'",
)

CSP_REPORT_ONLY = config('CSP_REPORT_ONLY', default=False)

# Exclude CMS admin from CSP
CSP_EXCLUDE_URL_PREFIXES = ('/cms-admin',)


# Cache
CACHES = {
    'default': {
        'BACKEND': config('CACHE_BACKEND',
                          default='django.core.cache.backends.memcached.MemcachedCache'),
        'LOCATION': config('CACHE_URL', default='127.0.0.1:11211'),
    }
}
##################
# Wagtail Settings
##################

WAGTAIL_SITE_NAME = 'coss'

# This is the bottom of settings.py
if 'test' in sys.argv[1:2]:
    SECURE_SSL_REDIRECT = False


#####################
# DEV, DEBUG Settings
#####################

if config('DEV', cast=bool, default=False):
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_URL = '/media/'
