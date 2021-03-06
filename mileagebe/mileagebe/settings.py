import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_DIR = os.path.normpath(os.path.join(BASE_DIR, '..'))

try:
    sensitive_settings = json.load(open('%s/configuration.json' % APP_DIR))
except:
    from mileagebe.fake_sensitive_settings import (
        SENSITIVE_SETTINGS as sensitive_settings)

SECRET_KEY = sensitive_settings['SECRET_KEY']
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'rest_framework',
    'csrf',
    'extended_user',
    'strava_client',
    'activities',
    'gear',
    'django_nose'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'strava_client.middleware.StravaQueryParamFixMiddleware'
)

ROOT_URLCONF = 'mileagebe.urls'
WSGI_APPLICATION = 'mileagebe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': sensitive_settings['DB_CONFIG']
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = sensitive_settings['STATIC_ROOT']

# Use the xff, using proxy
USE_X_FORWARDED_HOST = True

# URL for Strava API
STRAVA_BASE_URI = 'https://www.strava.com/api/v3/'

# Strava OAuth Configuration:
SOCIAL_AUTH_STRAVA_KEY = sensitive_settings['SOCIAL_AUTH_STRAVA_KEY']
SOCIAL_AUTH_STRAVA_SECRET = sensitive_settings['SOCIAL_AUTH_STRAVA_SECRET']
AUTHENTICATION_BACKENDS = (
    'social.backends.strava.StravaOAuth',
    'django.contrib.auth.backends.ModelBackend'
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/#mileage'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/#auth-error'
SOCIAL_AUTH_LOGIN_URL = '/#login'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/#profile'

AUTH_USER_MODEL = 'extended_user.ExtendedUser'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
