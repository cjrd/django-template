"""
Django settings for project_template project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'compressor',
    'devserver',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project_template.urls'

WSGI_APPLICATION = 'project_template.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# TODO consider moving hard coded dev dir
LOCAL_DEV_DIR = os.path.join(BASE_DIR, "local_dev")
if not os.path.exists(LOCAL_DEV_DIR):
    os.mkdir(LOCAL_DEV_DIR)
    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(LOCAL_DEV_DIR,'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "static"

# Additional locations of static files
STATICFILES_DIRS = (
    ('css',os.path.join(BASE_DIR, 'static/css')),
    ('imgs',os.path.join(BASE_DIR, 'static/imgs')),
    ('js',os.path.join(BASE_DIR, 'static/js')),
    ('fonts',os.path.join(BASE_DIR, 'static/fonts')),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates")
)

# for precompiling nonstandard content, e.g. scss
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

INTERNAL_IPS = ('127.0.0.1',)

from settings_local import *
