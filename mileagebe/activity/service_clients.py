import requests
from django.conf import settings


class StravaServiceClient(object):
    def get_user_data(self, user):
        extra_data = user.social_auth.get(provider='strava').extra_data
        access_token = extra_data['access_token']
        uri = '%s%s' % (settings.STRAVA_BASE_URI, 'athlete')

        response = requests.get(uri, params={
            'access_token': access_token
        })

        return response.json()
