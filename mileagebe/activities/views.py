from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
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
        request.DATA['user'] = reverse(
            'extendeduser-detail', args=[request.user.id], request=request)
        return super(ActivityList, self).create(request, *args, **kwargs)


class ActivityDetail(RetrieveUpdateDestroyAPIView):
    model = Activity
    serializer_class = ActivitySerializer
