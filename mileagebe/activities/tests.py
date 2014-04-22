from django.test import TestCase
from mock import Mock, patch

from activities.service_clients import StravaServiceClient


class ServiceClientTests(TestCase):
    def setUp(self):
        self.requests_patcher = patch('activities.service_clients.requests')
        self.requests = self.requests_patcher.start()

        self.user = Mock()
        self.auth_model = Mock(extra_data={'access_token': 123})

        def get(provider=None):
            return self.auth_model

        self.user.social_auth.get = get
        self.data = {'some': 'data'}
        self.requests.get.return_value = Mock(json=lambda: self.data)
        self.actual_data = StravaServiceClient.get_user_data(self.user)

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
