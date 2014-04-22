from rest_framework.views import APIView
from rest_framework.response import Response
from activities.service_clients import StravaServiceClient


class StravaUser(APIView):
    def get(self, request):
        service_client = StravaServiceClient()
        strava_user = service_client.get_user_data(request.user)

        return Response(strava_user)


class StravaActivities(APIView):
    def get(self, request):
        service_client = StravaServiceClient()
        activities = service_client.get_activities(request.user)

        return Response(activities)


class StravaGear(APIView):
    def get(self, request, gear_id):
        service_client = StravaServiceClient()
        activities = service_client.get_gear(request.user, gear_id)

        return Response(activities)
