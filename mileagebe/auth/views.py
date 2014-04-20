from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import LoginSerializer


class Session(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.DATA)

        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.data['username']
        password = serializer.data['password']

        return self.login(request, username, password)

    def login(self, request, username, password):

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
            return Response({'success': True})

        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        logout(request)
        return Response({'success': True})


class AuthCheck(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response({'success': True})
