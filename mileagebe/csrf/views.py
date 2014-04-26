from django.core.context_processors import csrf
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class Csrf(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        csrf_token = csrf(request)
        csrf_token['csrf_token'] = unicode(csrf_token['csrf_token'])
        return Response(csrf_token)
