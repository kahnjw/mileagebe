from rest_framework import viewsets

from gear.models import Gear
from gear.serializers import GearSerializer


class GearViewSet(viewsets.ModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializer
