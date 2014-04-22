import requests
from django.conf import settings


class StravaServiceClient(object):

    @classmethod
    def _build_uri(cls, endpoint):
        return '%s%s' % (settings.STRAVA_BASE_URI, endpoint)

    @classmethod
    def _make_request(cls, user, endpoint):
        extra_data = user.social_auth.get(provider='strava').extra_data
        access_token = extra_data['access_token']

        return requests.get(cls._build_uri(endpoint), params={
            'access_token': access_token
        })

    @classmethod
    def get_user_data(cls, user, metric=True):
        return cls._make_request(user, 'athlete').json()

    @classmethod
    def get_activities(cls, user, metric=False):
        return cls._make_request(user, 'activities').json()

    @classmethod
    def get_gear(cls, user, gear_id, metric=True):
        return cls._make_request(user, 'gear/%s' % gear_id).json()
