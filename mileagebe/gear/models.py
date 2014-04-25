from django.db import models


class Gear(models.Model):
    name = models.CharField(max_length=255)
    untracked_mileage = models.FloatField(default=0)
    lifetime = models.FloatField(default=2000)
    activities = models.ManyToManyField(
        'activities.Activity', related_name='gear')

    def get_miles_left(self):
        return self.lifetime - self.get_mileage()

    def get_mileage(self):
        activities = self.activities.all()
        miles = 0

        for activity in activities:
            miles += activity.distance

        return miles + self.untracked_mileage
