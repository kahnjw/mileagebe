import requests
from django.conf import settings


class StravaServiceClient(object):
    def _build_uri(self, endpoint):
        return '%s%s' % (settings.STRAVA_BASE_URI, endpoint)

    def _make_request(self, user, endpoint):
        extra_data = user.social_auth.get(provider='strava').extra_data
        access_token = extra_data['access_token']

        return requests.get(self._build_uri(endpoint), params={
            'access_token': access_token
        })

    def get_user_data(self, user):
        return self._make_request(user, 'athlete').json()

    def get_activities(self, user):
        return self._make_request(user, 'activities').json()
