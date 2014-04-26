from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.reverse import reverse


from gear.models import Gear
from gear.serializers import GearSerializer


class GearList(ListCreateAPIView):
    serializer_class = GearSerializer

    def get_queryset(self):
        return Gear.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        request.DATA['user'] = reverse(
            'extendeduser-detail', args=[request.user.id], request=request)
        return super(GearList, self).create(request, *args, **kwargs)


class GearDetail(RetrieveUpdateDestroyAPIView):
    model = Gear
    serializer_class = GearSerializer
