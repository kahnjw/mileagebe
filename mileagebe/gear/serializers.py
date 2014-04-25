from rest_framework import serializers

from gear.models import Gear


class GearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gear
        fields = ('name', 'untracked_mileage', 'lifetime', 'activities')
