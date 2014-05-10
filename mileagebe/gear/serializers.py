from rest_framework import serializers

from gear.models import Gear


class GearSerializer(serializers.HyperlinkedModelSerializer):
    total_mileage = serializers.Field(source='get_mileage')
    miles_left = serializers.Field(source='get_miles_left')

    class Meta:
        model = Gear
        fields = ('name', 'untracked_mileage', 'lifetime', 'user', 'url',
                  'activities', 'total_mileage', 'miles_left', 'id')
