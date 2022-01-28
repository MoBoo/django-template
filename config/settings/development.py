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

# Whitenoise
# ----------------------------------------------------------------------------------------------------------------------
# Disable Djangos runserver static files serving, and use whitenoise instead
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS

# Django Debug Toolbar
# ----------------------------------------------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}

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
