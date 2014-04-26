import json

from django.test import TestCase, RequestFactory
from mock import Mock, patch
from pint import UndefinedUnitError

from strava_client.service_clients import StravaServiceClient
from strava_client.views import StravaUser, StravaActivities


class ServiceClientBaseTestSetup(TestCase):
    def setUp(self, data=None):
        self.data = data or self.data
        self.requests_patcher = patch('strava_client.service_clients.requests')
        self.requests = self.requests_patcher.start()

        self.user = Mock()
        self.auth_model = Mock(extra_data={'access_token': 123})

        def get(provider=None):
            return self.auth_model

        self.user.social_auth.get = get
        self.requests.get.return_value = Mock(json=lambda: self.data)
        self.actual_data = StravaServiceClient.get_user_data(self.user)


class ServiceClientTests(ServiceClientBaseTestSetup):
    def setUp(self):
        data = {'some': 'data'}
        super(ServiceClientTests, self).setUp(data)

    def test_calls_requests_get_function(self):
        self.actual_data = StravaServiceClient.get_user_data(self.user)
        self.assertEqual(self.actual_data, self.data)

    def test_get_user_data_calls_requests_with_correct_params(self):
        self.actual_data = StravaServiceClient.get_user_data(self.user)
        self.requests.get.assert_called_with(
            'https://www.strava.com/api/v3/athlete',
            params={'access_token': 123})

    def test_get_activities_calls_requests_with_correct_params(self):
        self.actual_data = StravaServiceClient.get_activities(self.user)
        self.requests.get.assert_called_with(
            'https://www.strava.com/api/v3/activities',
            params={'access_token': 123})

    def test_get_gear_calls_requests_with_correct_params(self):
        self.actual_data = StravaServiceClient.get_gear(self.user, '123')
        self.requests.get.assert_called_with(
            'https://www.strava.com/api/v3/gear/123',
            params={'access_token': 123})


class ServiceClientUnitConversionTests(ServiceClientBaseTestSetup):
    def setUp(self):
        data = [
            {
                'distance': 16029.34,
                'average_temp': 24,
                'max_speed': 10

            },
            {
                'distance': 54.34,
                'average_temp': 21,
                'max_speed': 7
            }
        ]
        super(ServiceClientUnitConversionTests, self).setUp(data)
        self.actual_data = StravaServiceClient.get_activities(
            self.user, distance='miles')

    def test_meters_converts_to_miles(self):
        self.assertEqual(self.actual_data[0]['distance'], 9.96)

    def test_meters_second_to_miles_per_hour(self):
        self.actual_data = StravaServiceClient.get_activities(
            self.user, max_speed=('miles', 'hour'))
        self.assertEqual(self.actual_data[0]['max_speed'], 22.37)

    def test_does_not_affect_other_data(self):
        self.assertEqual(self.actual_data[0]['average_temp'], 24)

    def test_raises_bad_units_with_given_bad_unit_string(self):
        self.assertRaises(UndefinedUnitError,
                          StravaServiceClient.get_activities, self.user,
                          distance='bad_unit')


class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('fake/url')

        self.client_pather = patch('strava_client.views.StravaServiceClient')
        self.client = self.client_pather.start()

        self.client.get_user_data.return_value = {'user': 'data'}
        self.client.get_activities.return_value = {'distance': 10}
        self.client.get_gear.return_value = {'gear': 'data'}

    def test_strava_user_endpoint_returns_user_data(self):
        response = StravaUser.as_view()(self.request)
        response.render()
        self.assertEqual(json.loads(response.content), {'user': 'data'})

    def test_strava_activities_endpoint_returns_activities_data(self):
        response = StravaActivities.as_view()(self.request)
        response.render()
        self.assertEqual(json.loads(response.content), {'distance': 10})

    def test_strava_activities_endpoint_takes_query_parameters(self):
        request = self.factory.get('fake/url', {
            'distance': 'miles',
            'max_speed': 'miles.hour'
        })
        request.user = 'user'
        StravaActivities.as_view()(request)
        self.client.get_activities.assert_called_with(
            request.user, distance='miles', max_speed=['miles', 'hour'])

