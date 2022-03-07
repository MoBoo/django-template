from .base import *
from .base import env

# General Settings
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#debug
DEBUG = True  # Enable DEBUG explicitly for development

# https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY", default="DEVELOPMENT_DJANGO_SECRET_KEY")

# https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

# Database Config
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(PROJECT_ROOT / 'dev.sqlite3'),
    }
}

# Email Config
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/email/#console-
# based on https://github.com/joke2k/django-environ/issues/7#issuecomment-54299158
EMAIL_CONFIG = env.email("DJANGO_EMAIL_SMTP_CONNECTION_STRING", default="consolemail://")
vars().update(EMAIL_CONFIG)

# Static Content
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
STATIC_ROOT = str(PROJECT_ROOT / 'staticfiles')

# https://docs.djangoproject.com/en/4.0/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(PROJECT_ROOT / '/'.join(app_name.split(".")) / 'static') for app_name in CUSTOM_APPS]

# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media Content
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#media-root
MEDIA_ROOT = str(PROJECT_ROOT / 'mediafiles')

# https://docs.djangoproject.com/en/4.0/ref/settings/#media-url
MEDIA_URL = '/media/'
