from rest_framework import serializers

from activities.models import Activity


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    nice_moving_time = serializers.Field(source='get_nice_moving_time')
    nice_start_date = serializers.Field(source='get_nice_start_date')

    class Meta:
        model = Activity
        fields = ('url', 'strava_id', 'location_city', 'distance', 'gear',
                  'max_speed', 'average_speed', 'total_elevation_gain', 'user',
                  'moving_time', 'name', 'nice_moving_time',
                  'nice_start_date', 'id')
