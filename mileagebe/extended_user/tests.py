import json

from django.test import TestCase, RequestFactory

from extended_user.serializers import ExtendedUserSerializer
from extended_user.views import ExtendedUserList, Me
from extended_user.models import ExtendedUser


class ExtendedUserSerializerTests(TestCase):
    def setUp(self):
        user = ExtendedUser.objects.create_user(
            username='Bob', password='Saget')
        self.serializer = ExtendedUserSerializer(user)

    def test_returns_url_fields(self):
        self.assertEqual(self.serializer.data['url'], '/api/v1/users/1')

    def test_returns_username_field(self):
        self.assertEqual(self.serializer.data['username'], 'Bob')


class ExtendedUserListTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        data = {
            'username': 'Bob',
            'password': 'Saget'
        }

        request = self.factory.post('/api/v1/users/', data, format='json')
        response = ExtendedUserList.as_view()(request)
        response.render()
        self.response_body = json.loads(response.content)

    def test_endpoint_saves_a_user_to_the_database(self):
        ExtendedUser.objects.get(username='Bob')

    def test_endopint_returns_user_representation(self):
        self.assertEqual(self.response_body['username'], 'Bob')
        self.assertEqual(self.response_body['url'], '/api/v1/users/1')

    def test_endopint_returns_400_on_bad_input(self):
        data = {
            'username': '',
            'password': 'Saget'
        }
        request = self.factory.post('/api/v1/users/', data, format='json')
        response = ExtendedUserList.as_view()(request)
        self.assertEqual(response.status_code, 400)


class MeEndpointTests(TestCase):
    def setUp(self):
        factory = RequestFactory()
        data = {
            'username': 'Bob',
            'password': 'Saget'
        }

        request = factory.get('/api/v1/me/', data, format='json')
        request.user = ExtendedUser.objects.create_user(
            username='Bob', password='Saget')
        response = Me.as_view()(request)
        response.render()
        self.response_body = json.loads(response.content)

    def test_returns_a_user_representation(self):
        self.assertEqual(self.response_body['username'], 'Bob')
        self.assertEqual(self.response_body['url'], '/api/v1/users/1')
