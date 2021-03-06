"""
Django settings for sniffer project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os

# import pyodbc

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4p7rgv7pc7su9mn_z^3-bu$!0$xyqb!k6)w3*d5#1i$@2c36gi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sniffer',
    'statSVN',
    'rail',
    'way',
    'result',
    # 'tdoa',
    'qualityS',
    'maui',
    'misoa',
    'a',
    # 'django_celery_results',
    # 'kombu.transport.django',
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

ROOT_URLCONF = 'sniffer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sniffer.wsgi.application'

MSSQL_OPTIONS = {
    # 'driver': 'SQL Native Client',
    # 'driver': 'SQL Server Native Client 11.0',
    # 'driver': 'SQL Server Native Client 10.0',#sql server2008
    # 'host_is_server': True,
    # 'extra_params': "TDS_VERSION=8.0",
    'driver_needs_utf8': True,
    'encoding': "utf-8",
    'timeout': 30,
    # added the time out as i was getting issue with connections being dropped and errors being raised, since adding this the issues have gone.
}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'ENGINE': 'django_mysqlpool.backends.mysqlpool',
        'NAME': 'sniffer',
        # 'NAME': 'sniffer_dev',
        'USER': ' ',
        'PASSWORD': 'O6=7) *7',
        'HOST': '10.32',
        'PORT': '3336',
        'OPTIONS': {'charset': 'utf8mb4'},

    },
    'svn': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'svn',
        'USER': 'zhaochunyu',
        'PASSWORD': '=n3Z',
        'HOST': '10.32',
        'PORT': '3306',
        # 'default-character-set' ='utf8',
    },
    'misoa': {
        'ENGINE': 'sqlserver_pymssql',
        'NAME': 'ecology',
        'USER': 'devpr',
        'PASSWORD': 'Q!',
        'HOST': '19',
        'PORT': '1433',
        # 'OPTIONS': MSSQL_OPTIONS,
        # 'default-character-set' ='utf8',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './tmp/way.log',  # 或者直接写路径：'c:\logs\all.log',
            'maxBytes': 1024 * 1024 * 20,  # 20 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 20,  # 20 MB
            'backupCount': 5,
            'filename': './tmp/result.log',
            'formatter': 'standard'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './tmp/error.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'formatter': 'standard',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'qualityS': {
            'handlers': ['error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'way': {
            'handlers': ['default', 'console', 'error'],
            'level': 'INFO',
            'propagate': True
        },
        'rail': {
            'handlers': ['default', 'console', 'error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'maui': {
            'handlers': ['default', 'console', 'error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'misoa': {
            'handlers': ['default', 'console', 'error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'result': {
            'handlers': ['console', 'error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'a': {
            'handlers': ['console', 'error', 'file_handler'],
            'level': 'INFO',
            'propagate': True
        },

    }
}

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
ALLOWED_HOSTS = ['10.37.5.26', '127.0.0.1']

LOGIN_URL = '/admin/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
