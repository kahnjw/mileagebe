from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from extended_user.models import ExtendedUser
from extended_user.serializers import ExtendedUserSerializer, LoginSerializer


class ExtendedUserList(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer

    def create(self, request, *args, **kwargs):
        username = request.DATA['username']
        password = request.DATA['password']
        try:
            ext_user = ExtendedUser.objects.create_user(
                username, password=password)
            serialized_user = self.serializer_class(ext_user)

        except ValueError:
            error = {'error': 'BAD_INPUT'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            serialized_user.data, status=status.HTTP_201_CREATED)


class ExtendedUserDetail(RetrieveUpdateDestroyAPIView):
    model = ExtendedUser
    serializer_class = ExtendedUserSerializer


class Me(APIView):
    serializer_class = ExtendedUserSerializer

    def get(self, request):
        if request.user.is_anonymous():
            raise Http404()

        serialized_user = self.serializer_class(request.user)

        return Response(serialized_user.data)


class Session(APIView):
    permission_classes = (AllowAny,)

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
            return Response({
                'success': True
            }, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        logout(request)
        return Response({'success': True})
