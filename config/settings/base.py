import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
APPS_DIR = PROJECT_ROOT / 'apps'

env = environ.Env(
    DEBUG=(bool, False)
)
# Read .env variables into environment variables
READ_ENV_FILE = env('DJANGO_USE_ENV_FILE', default=False)
if READ_ENV_FILE:
    env.read_env(str(PROJECT_ROOT / '.env'))

# General Settings
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', default=False)  # make sure DEBUG is never accidentally enabled in production

# Internationalization (https://docs.djangoproject.com/en/4.0/topics/i18n/)
# ----------------------------------------------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/4.0/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/4.0/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/4.0ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#locale-paths
LOCALE_PATHS = [str(PROJECT_ROOT / 'locale')]

# Database
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Database Migrations
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#migration-modules
MIGRATION_MODULES = {'sites': '{{ cookiecutter.project_slug }}.contrib.sites.migrations'}

# Url Config
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'

# https://docs.djangoproject.com/en/4.0/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# Apps
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#installed-apps

BASE_DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# https://www.django-rest-framework.org/
# https://pypi.org/project/django-cors-headers/
# https://djoser.readthedocs.io/en/latest/getting_started.html
BASE_3RD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser'
]

CUSTOM_APPS = [

]

INSTALLED_APPS = BASE_DJANGO_APPS + BASE_3RD_PARTY_APPS + CUSTOM_APPS

# Middleware
# ----------------------------------------------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Security
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/4.0/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# Authentication
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/auth/passwords/#auth-password-storage
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Logging
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/topics/logging/
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Static Content
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#static-root
STATIC_ROOT = str(PROJECT_ROOT / 'staticfiles')

# https://docs.djangoproject.com/en/4.0/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / '/'.join(app_name.split(".")) / 'static') for app_name in CUSTOM_APPS]

# https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Media Content
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / 'mediafiles')

# https://docs.djangoproject.com/en/4.0/ref/settings/#media-url
MEDIA_URL = '/media/'

# Templates
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.0/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # https://docs.djangoproject.com/en/4.0/ref/settings/#dirs
        'DIRS': [str(APPS_DIR / 'templates')],
        # https://docs.djangoproject.com/en/4.0/ref/settings/#app-dirs
        'APP_DIRS': True,
        # https://docs.djangoproject.com/en/4.0/topics/templates/#django.template.backends.django.DjangoTemplates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Django Admin
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMIN_URL = "admin/"

# Django Rest Framework
# ----------------------------------------------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# Django Cors Header
# ----------------------------------------------------------------------------------------------------------------------
# https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_ORIGIN_REGEXES = []
