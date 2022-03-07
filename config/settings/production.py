from .base import *
from .base import env

# General Settings
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#debug
DEBUG = False  # Disable DEBUG for production

# https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")  # raise exception if not set in production

# https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

# Database Config
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': env.db("DJANGO_DATABASE_CONNECTION_STRING"),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = env.int("DJANGO_DATABASE_CONN_MAX_AGE", default=60)

# Caching
# ----------------------------------------------------------------------------------------------------------------------
CACHES = {
    'default': env.cache('DJANGO_CACHE_URL')
}
# Do not raise exceptions when redis is down (https://github.com/jazzband/django-redis#memcached-exceptions-behavior)
CACHES['default']['IGNORE_EXCEPTIONS'] = True

# Security
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-ssl-redirect
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

# https://docs.djangoproject.com/en/4.0/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True

# https://docs.djangoproject.com/en/4.0/topics/security/#ssl-https
# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-seconds
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60

# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-include-subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)

# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-hsts-preload
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

# https://docs.djangoproject.com/en/4.0/ref/middleware/#x-content-type-options-nosniff
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)

# Email Config
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# based on https://github.com/joke2k/django-environ/issues/7#issuecomment-54299158
EMAIL_CONFIG = env.email("DJANGO_EMAIL_SMTP_CONNECTION_STRING")
vars().update(EMAIL_CONFIG)

# https://docs.djangoproject.com/en/4.0/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL", default="Things n' Stuff <noreply@django_template.app>")

# https://docs.djangoproject.com/en/4.0/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default="Things n' Stuff Admin <admin@django_template.app>")

# https://docs.djangoproject.com/en/4.0/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env("DJANGO_EMAIL_SUBJECT_PREFIX", default="[Things n' Stuff]")

# Admin
# ----------------------------------------------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL", default=ADMIN_URL)

# # Cloud storage
# # --------------------------------------------------------------------------------------------------------------------
# # https://django-storages.readthedocs.io/en/latest/#installation
# INSTALLED_APPS += ["storages"]
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_QUERYSTRING_AUTH = False
#
# # DO NOT change these unless you know what you're doing.
# _AWS_EXPIRY = 60 * 60 * 24 * 7
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
# }
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
#
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
# AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default=None)
# aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
#
# # Static Content
# # --------------------------------------------------------------------------------------------------------------------
# STATICFILES_STORAGE = "utils.storages.StaticRootS3Boto3Storage"
# COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"
# STATIC_URL = f"https://{aws_s3_domain}/static/"
# TODO: STATIC_URL for local nginx

# # Media Content
# # --------------------------------------------------------------------------------------------------------------------
# DEFAULT_FILE_STORAGE = "utils.storages.MediaRootS3Boto3Storage"
# MEDIA_URL = f"https://{aws_s3_domain}/media/"
# TODO: MEDIA_URL for local nginx

# Logging
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/logging/
# Sample logging configuration: send email notification to admins on HTTP 500 Errors
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

# Django Rest Framework
# ----------------------------------------------------------------------------------------------------------------------
# Disable browsable API for production
# REST_FRAMEWORK = {
#     "DEFAULT_RENDERER_CLASSES": [
#         'rest_framework.renderers.JSONRenderer',
#     ]
# }
