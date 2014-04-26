from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class Root(APIView):
    def get(self, request):
        activities = reverse('activity-list', request=request)
        users = reverse('extendeduser-list', request=request)
        gear = reverse('gear-list', request=request)
        csrf = reverse('csrf', request=request)

        data = {
            'activities': activities,
            'users': users,
            'gear': gear,
            'csrf': csrf
        }

        return Response(data)
