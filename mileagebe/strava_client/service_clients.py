import json
import os
import requests

from django.conf import settings
from pint import UnitRegistry, UndefinedUnitError

APP_PATH = os.path.abspath(os.path.dirname(__file__))


class StravaServiceClient(object):
    ureg = UnitRegistry()
    units_mapping_file = open('%s/units_mapping.json' % APP_PATH)
    units_mapping = json.load(units_mapping_file)

    @classmethod
    def _build_uri(cls, endpoint):
        return '%s%s' % (settings.STRAVA_BASE_URI, endpoint)

    @classmethod
    def _convert(cls, data, endpoint, **convs):
        units_subset = cls.units_mapping[endpoint]
        for conv in convs:
            original_unit = cls._get_unit(units_subset[conv])

            try:
                new_unit = cls._get_unit(convs[conv])
            except UndefinedUnitError:
                message = '%s is not a valid unit' % convs[conv]
                raise UndefinedUnitError(message)

            original_data_point = data[conv] * original_unit
            converted_data_point = original_data_point.to(new_unit)

            data[conv] = round(converted_data_point.magnitude, 2)

        return data

    @classmethod
    def _get_unit(cls, unit):
        if type(unit) is tuple or type(unit) is list:
            return getattr(cls.ureg, unit[0]) / getattr(cls.ureg, unit[1])

        return getattr(cls.ureg, unit)

    @classmethod
    def _make_request(cls, user, endpoint):
        social_user = user.social_auth.filter(provider='strava')[0]
        access_token = social_user.extra_data['access_token']

        return requests.get(cls._build_uri(endpoint), params={
            'access_token': access_token
        })

    @classmethod
    def get_user_data(cls, user, **convs):
        data = cls._make_request(user, 'athlete').json()

        if convs:
            return cls._convert(data, 'user_data', **convs)
        return data

    @classmethod
    def get_activities(cls, user, **convs):
        data = cls._make_request(user, 'activities').json()

        if not convs:
            return data

        return [cls._convert(act, 'activities', **convs) for act in data]

    @classmethod
    def get_gear(cls, user, gear_id, **convs):
        data = cls._make_request(user, 'gear/%s' % gear_id).json()

        if convs:
            return cls._convert(data, 'gear', **convs)
        return data
