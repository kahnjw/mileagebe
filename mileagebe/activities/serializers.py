from rest_framework import serializers

from activities.models import Activity


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('url', 'strava_id', 'location_city', 'distance', 'gear',
                  'max_speed', 'average_speed', 'total_elevation_gain', 'user',
                  'moving_time')
