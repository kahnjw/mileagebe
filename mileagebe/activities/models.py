import datetime

from django.db import models

from strava_client.service_clients import StravaServiceClient


class ActivityManager(models.Manager):
    def refresh(self, user):
        raw_acts = StravaServiceClient.get_activities(
            user, distance='miles', max_speed=('miles', 'hour'),
            average_speed=('miles', 'hour'), total_elevation_gain='feet')
        return [self._save_activity(user, raw_act) for raw_act in raw_acts]

    def _save_activity(self, user, raw_act):
        import pprint
        pprint.pprint(raw_act)
        activity, created = Activity.objects.get_or_create(
            user=user, strava_id=raw_act['id'])

        if created:
            activity.name = raw_act.get('name')
            activity.activity_type = raw_act.get('type')
            activity.location_city = raw_act.get('location_city')
            activity.distance = raw_act.get('distance')
            activity.moving_time = raw_act.get('moving_time')
            activity.max_speed = raw_act.get('max_speed')
            activity.average_speed = raw_act.get('average_speed')
            activity.total_elevation_gain = raw_act.get('total_elevation_gain')
            activity.start_date_time = raw_act.get('start_date_local')
            activity.save()

        return activity


class Activity(models.Model):
    objects = ActivityManager()

    user = models.ForeignKey(
        'extended_user.ExtendedUser', related_name='activities')

    name = models.CharField(max_length=1024, null=True, blank=True)
    activity_type = models.CharField(max_length=255, null=True, blank=True)
    strava_id = models.CharField(max_length=255, null=True, blank=True)
    location_city = models.CharField(max_length=255)
    distance = models.FloatField(default=0)
    moving_time = models.FloatField(default=0)
    max_speed = models.FloatField(default=0)
    average_speed = models.FloatField(default=0)
    total_elevation_gain = models.FloatField(default=0)
    start_date_time = models.CharField(max_length=255)

    def get_nice_moving_time(self):
        return str(datetime.timedelta(seconds=self.moving_time))

    def get_nice_start_date(self):
        if not self.start_date_time:
            return ''

        time = datetime.datetime.strptime(
            self.start_date_time, '%Y-%m-%dT%H:%M:%SZ')
        return '%s/%s/%s' % (time.month, time.day, time.year)
