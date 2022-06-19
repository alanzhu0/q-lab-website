from pathlib import Path

from django.urls import reverse_lazy


# Basic settings

BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Application definition

INSTALLED_APPS = [
    'social_django',
    'qlab.apps.base',
    'qlab.apps.projects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qlab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'qlab.wsgi.application'


# Password validation

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


# Authentication

AUTH_USER_MODEL = 'base.User'

CSRF_TRUSTED_ORIGINS = ['https://qlab.sites.tjhsst.edu']

LOGIN_REDIRECT_URL = reverse_lazy("base:index")

LOGOUT_REDIRECT_URL = reverse_lazy("base:index")

LOGIN_URL = reverse_lazy("base:login")

SOCIAL_AUTH_ALWAYS_ASSOCIATE = True

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.auth_allowed",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
)

SOCIAL_AUTH_URL_NAMESPACE = "social"

SOCIAL_AUTH_USER_FIELDS = [
    "first_name",
    "graduation_year",
    "id",
    "is_staff",
    "is_superuser",
    "last_name",
    "username",
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files

STATIC_ROOT = BASE_DIR / 'serve/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR / 'static/',
)


# Media files

MEDIA_ROOT = BASE_DIR / 'media/'

MEDIA_URL = '/media/'


# Import secret.py
from .secret import *
