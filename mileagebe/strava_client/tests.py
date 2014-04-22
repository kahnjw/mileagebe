import json

from django.test import TestCase, RequestFactory
from mock import Mock, patch

from strava_client.service_clients import StravaServiceClient
from strava_client.views import StravaUser, StravaActivities, StravaGear


class ServiceClientTests(TestCase):
    def setUp(self):
        self.requests_patcher = patch('strava_client.service_clients.requests')
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


class ViewsTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('fake/url')

        self.client_pather = patch('strava_client.views.StravaServiceClient')
        self.client = self.client_pather.start()

        self.client.get_user_data.return_value = {'user': 'data'}
        self.client.get_activities.return_value = {'activities': 'data'}
        self.client.get_gear.return_value = {'gear': 'data'}

    def test_strava_user_endpoint_returns_user_data(self):
        response = StravaUser.as_view()(self.request)
        response.render()
        self.assertEqual(json.loads(response.content), {'user': 'data'})

    def test_strava_activities_endpoint_returns_activities_data(self):
        response = StravaActivities.as_view()(self.request)
        response.render()
        self.assertEqual(json.loads(response.content), {'activities': 'data'})

    def test_strava_gear_endpoint_returns_gear_data(self):
        response = StravaGear.as_view()(self.request, '123')
        response.render()
        self.assertEqual(json.loads(response.content), {'gear': 'data'})
