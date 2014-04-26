from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.reverse import reverse


from gear.models import Gear
from gear.serializers import GearSerializer


class GearList(ListCreateAPIView):
    serializer_class = GearSerializer

    def get_queryset(self):
        return Gear.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.DATA.copy()
        data['user'] = reverse(
            'extendeduser-detail', args=[request.user.id], request=request)
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GearDetail(RetrieveUpdateDestroyAPIView):
    model = Gear
    serializer_class = GearSerializer
