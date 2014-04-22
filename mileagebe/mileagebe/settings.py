"""
Django settings for mileagebe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
try:
    from mileagebe import sensitive_settings
except:
    from mileagebe import fake_sensitive_settings as sensitive_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = sensitive_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

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
    'django_nose'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auth.middleware.StravaQueryParamFixMiddleware'
)

ROOT_URLCONF = 'mileagebe.urls'

WSGI_APPLICATION = 'mileagebe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

# Use the xff, using proxy
USE_X_FORWARDED_HOST = True

# URL for Strava API
STRAVA_BASE_URI = 'https://www.strava.com/api/v3/'

# Strava OAuth Configuration:
SOCIAL_AUTH_STRAVA_KEY = sensitive_settings.SOCIAL_AUTH_STRAVA_KEY
SOCIAL_AUTH_STRAVA_SECRET = sensitive_settings.SOCIAL_AUTH_STRAVA_SECRET
AUTHENTICATION_BACKENDS = sensitive_settings.SOCIAL_AUTH_AUTHENTICATION_BACKENDS

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/#mileage'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/#auth-error'
SOCIAL_AUTH_LOGIN_URL = '/#login'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/#authenticate'
SOCIAL_AUTH_USER_MODEL = 'extended_user.ExtendedUser'
AUTH_USER_MODEL = 'extended_user.ExtendedUser'
