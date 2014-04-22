SECRET_KEY = 'key'
SOCIAL_AUTH_STRAVA_KEY = '123456'
SOCIAL_AUTH_STRAVA_SECRET = 'secret'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social.backends.strava.StravaOAuth',
    'django.contrib.auth.backends.ModelBackend'
)
