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
    def _convert(cls, data, endpoint, **conversions):
        units_subset = cls.units_mapping[endpoint]
        for conversion in conversions:
            original_unit = cls._get_unit(units_subset[conversion])

            try:
                new_unit = cls._get_unit(conversions[conversion])
            except UndefinedUnitError:
                message = '%s is not a valid unit' % conversions[conversion]
                raise UndefinedUnitError(message)

            original_data_point = data[conversion] * original_unit
            converted_data_point = original_data_point.to(new_unit)

            data[conversion] = converted_data_point.magnitude

        return data

    @classmethod
    def _get_unit(cls, unit):
        if type(unit) is tuple or type(unit) is list:
            return getattr(cls.ureg, unit[0]) / getattr(cls.ureg, unit[1])

        return getattr(cls.ureg, unit)

    @classmethod
    def _make_request(cls, user, endpoint):
        extra_data = user.social_auth.get(provider='strava').extra_data
        access_token = extra_data['access_token']

        return requests.get(cls._build_uri(endpoint), params={
            'access_token': access_token
        })

    @classmethod
    def get_user_data(cls, user, **conversions):
        data = cls._make_request(user, 'athlete').json()

        if conversions:
            return cls._convert(data, 'user_data', **conversions)
        return data

    @classmethod
    def get_activities(cls, user, **conversions):
        data = cls._make_request(user, 'activities').json()

        if conversions:
            return cls._convert(data, 'activities', **conversions)
        return data

    @classmethod
    def get_gear(cls, user, gear_id, **conversions):
        data = cls._make_request(user, 'gear/%s' % gear_id).json()

        if conversions:
            return cls._convert(data, 'gear', **conversions)
        return data
