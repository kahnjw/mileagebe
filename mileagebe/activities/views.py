from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.reverse import reverse

from activities.models import Activity
from activities.serializers import ActivitySerializer


class ActivityList(ListCreateAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        refresh = request.QUERY_PARAMS.get('refresh')

        if refresh == 'true':
            Activity.objects.refresh(request.user)

        return super(ActivityList, self).list(request, *args, **kwargs)

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


class ActivityDetail(RetrieveUpdateDestroyAPIView):
    model = Activity
    serializer_class = ActivitySerializer
