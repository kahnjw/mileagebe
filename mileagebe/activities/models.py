from django.db import models

from strava_client.service_clients import StravaServiceClient


class ActivityManager(models.Manager):
    def refresh(self, user):
        raw_acts = StravaServiceClient.get_activities(
            user, distance='miles', max_speed=('miles', 'hour'),
            average_speed=('miles', 'hour'), total_elevation_gain='feet')
        return [self._save_activity(user, raw_act) for raw_act in raw_acts]

    def _save_activity(self, user, raw_act):
        activity, created = Activity.objects.get_or_create(
            user=user, strava_id=raw_act['id'])

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

    user = models.ForeignKey(
        'extended_user.ExtendedUser', related_name='activities')

    strava_id = models.CharField(max_length=255, null=True, blank=True)
    location_city = models.CharField(max_length=255)
    distance = models.FloatField(default=0)
    moving_time = models.FloatField(default=0)
    max_speed = models.FloatField(default=0)
    average_speed = models.FloatField(default=0)
    total_elevation_gain = models.FloatField(default=0)
