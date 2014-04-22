from rest_framework.views import APIView
from rest_framework.response import Response
from activities.service_clients import StravaServiceClient


class StravaUser(APIView):
    def get(self, request):
        strava_user = StravaServiceClient.get_user_data(request.user)

        return Response(strava_user)


class StravaActivities(APIView):
    def get(self, request):
        activities = StravaServiceClient.get_activities(request.user)

        return Response(activities)


class StravaGear(APIView):
    def get(self, request, gear_id):
        activities = StravaServiceClient.get_gear(request.user, gear_id)

        return Response(activities)
