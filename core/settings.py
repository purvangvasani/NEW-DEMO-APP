# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import environ
import dj_database_url

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='S#perS3crEt_007')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

# load production server from .env
ALLOWED_HOSTS = ['localhost', 'localhost:85', '127.0.0.1',
                 env('SERVER', default='127.0.0.1'), 'hire-exe.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1',
                        'https://' + env('SERVER', default='127.0.0.1')]

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'apps.home'  # Enable the inner home (home)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(
    CORE_DIR, "apps/templates")  # ROOT dir for templates


# Base url to serve media files
MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, MEDIA_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'apps.context_processors.cfg_assets_root',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# if os.environ.get('DB_ENGINE') and os.environ.get('DB_ENGINE') == "mysql":
#     DATABASES = {
#       'default': {
#         'ENGINE'  : 'django.db.backends.mysql',
#         'NAME'    : os.getenv('DB_NAME'     , 'appseed_db'),
#         'USER'    : os.getenv('DB_USERNAME' , 'appseed_db_usr'),
#         'PASSWORD': os.getenv('DB_PASS'     , 'pass'),
#         'HOST'    : os.getenv('DB_HOST'     , 'localhost'),
#         'PORT'    : os.getenv('DB_PORT'     , 3306),
#         },
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': 'db.sqlite3',
#         }
#     }

# DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.postgresql_psycopg2",

#         'NAME': "django_test",

#         'USER': "postgres",

#         'PASSWORD': "aspire@123",

#         'HOST': "localhost",

#         'PORT': "5432"
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",

        'NAME': "dfh80kloon3jsq",

        'USER': "ekguabdkcfxayh",

        'PASSWORD': "b69fcee555480c4aae4a12ee05802ac944df192bba8efef70f3dc3bef3e7d621",

        'HOST': "ec2-44-205-112-253.compute-1.amazonaws.com",

        'PORT': "5432"
    }
}

WHITENOISE_USE_FINDERS = True

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#############################################################
#############################################################
