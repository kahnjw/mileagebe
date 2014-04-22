from django.core.context_processors import csrf
from rest_framework.views import APIView
from rest_framework.response import Response


class Csrf(APIView):
    def get(self, request):
        csrf_token = csrf(request)
        csrf_token['csrf_token'] = unicode(csrf_token['csrf_token'])
        return Response(csrf_token)
