from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from extended_user.models import ExtendedUser
from gear.models import Gear
from gear.views import GearList


class GearModelTests(TestCase):
    def setUp(self):
        self.user = ExtendedUser.objects.create_user(
            username='Bob', password='Saget')
        self.chain = Gear.objects.create(
            name='chain', untracked_mileage=100, user=self.user)

    def test_get_miles_left_returns_correct_miles_left(self):
        self.assertEqual(self.chain.get_miles_left(), 1900)


class GearViewTests(TestCase):
    def configure_test(self, data=None):
        if data is None:
            data = {
                'name': 'Chain',
                'untracked_mileage': 5,
                'lifetime': 5,
            }

        self.factory = APIRequestFactory()
        self.request = Request(self.factory.post('/create_gear/', data))
        self.request.user = ExtendedUser.objects.create_user(
            username='Bob', password='Saget')

        self.response = GearList.as_view()(self.request)

    def test_it_creates_gear(self):
        self.configure_test()
        self.assertEqual(self.response.status_code, 201)

    def test_it_returns_bad_request_with_invalid_data(self):
        self.configure_test({'im': 'a bannana'})
        self.assertEqual(self.response.status_code, 400)
