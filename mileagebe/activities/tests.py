import json
import os

from django.test import TestCase
from mock import patch

from activities.models import Activity
from extended_user.models import ExtendedUser


APP_PATH = os.path.abspath(os.path.dirname(__file__))


class ActivityObjectsManagerTests(TestCase):
    def setUp(self):
        self.user = ExtendedUser.objects.create_user(
            username='Bob', password='Saget')
        self.raw_sample_data = open('%s/sample_activity_data.json' % APP_PATH)
        self.sample_data = json.load(self.raw_sample_data)

        self.client_patcher = patch('activities.models.StravaServiceClient')
        self.client = self.client_patcher.start()
        self.client.get_activities.return_value = self.sample_data

    def test_refresh_creates_new_objects(self):
        activities = Activity.objects.all()
        self.assertEqual(len(activities), 0)

        Activity.objects.refresh(self.user)
        activities = Activity.objects.all()
        self.assertEqual(len(activities), 3)

    def test_refresh_creates_new_objects3(self):
        Activity.objects.refresh(self.user)
        activities = Activity.objects.all()
        self.assertEqual(
            activities[0].strava_id, str(self.sample_data[0]['id']))
        self.assertEqual(
            activities[2].strava_id, str(self.sample_data[2]['id']))

    def test_refresh_does_not_duplicate_activity_entries(self):
        Activity.objects.refresh(self.user)
        activities = Activity.objects.all()
        self.assertEqual(len(activities), 3)

        Activity.objects.refresh(self.user)
        activities = Activity.objects.all()
        self.assertEqual(len(activities), 3)
