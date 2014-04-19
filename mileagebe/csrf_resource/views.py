from django.core.context_processors import csrf
from rest_framework.views import APIView
from rest_framework.response import Response


class Csrf(APIView):
    def get(self, request):
        return Response(csrf(request))
