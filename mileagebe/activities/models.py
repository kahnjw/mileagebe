from django.db import models

from strava_client.service_clients import StravaServiceClient


class ActivityManager(models.Manager):
    def refresh(self):
        raw_acts = StravaServiceClient.get_activities()
        return [self._save_activity(raw_act) for raw_act in raw_acts]

    def _save_activity(self, raw_act):
        activity, created = Activity.objects.get_or_create(
            strava_id=raw_act['id'])

        if created:
            activity.distance = raw_act['distance']
            activity.moving_time = raw_act['moving_time']
            activity.max_speed = raw_act['max_speed']
            activity.average_speed = raw_act['average_speed']
            activity.total_elevation_gain = raw_act['total_elevation_gain']
            activity.save()

        return activity


class Activity(models.Model):
    objects = ActivityManager()

    strava_id = models.CharField(max_length=255)
    location_city = models.CharField(max_length=255)
    distance = models.FloatField(default=0)
    moving_time = models.FloatField(default=0)
    max_speed = models.FloatField(default=0)
    average_speed = models.FloatField(default=0)
    total_elevation_gain = models.FloatField(default=0)
