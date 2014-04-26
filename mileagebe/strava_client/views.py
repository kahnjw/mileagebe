from rest_framework.views import APIView
from rest_framework.response import Response
from strava_client.service_clients import StravaServiceClient


class StravaBaseAPIView(APIView):
    def _process_conversions(self, conversions):
        parsed = {}
        for key in conversions:
            parsed[key] = conversions[key]
            if '.' in parsed[key]:
                parsed[key] = parsed[key].split('.', 1)

        return parsed


class StravaUser(StravaBaseAPIView):
    def get(self, request):
        strava_user = StravaServiceClient.get_user_data(request.user)

        return Response(strava_user)


class StravaActivities(StravaBaseAPIView):
    def get(self, request):
        conversions = self._process_conversions(request.QUERY_PARAMS)
        activities = StravaServiceClient.get_activities(
            request.user, **conversions)

        return Response(activities)
