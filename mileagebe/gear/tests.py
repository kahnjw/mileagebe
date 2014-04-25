from django.test import TestCase

from gear.models import Gear


class GearTests(TestCase):
    def setUp(self):
        self.chain = Gear.objects.create(name='chain', untracked_mileage=100)

    def test_get_miles_left_returns_correct_miles_left(self):
        self.assertEqual(self.chain.get_miles_left(), 1900)
