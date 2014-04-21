from rest_framework.views import APIView
from rest_framework.response import Response
from activity.service_clients import StravaServiceClient


class SocialUserList(APIView):
    def get(self, request):
        service_client = StravaServiceClient()
        social_user = service_client.get_user_data(request.user)

        return Response(social_user)
