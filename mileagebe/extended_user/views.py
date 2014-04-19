from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView, RetrieveAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response

from extended_user.models import ExtendedUser
from extended_user.serializers import ExtendedUserSerializer, UserSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExtendedUserList(ListCreateAPIView):
    queryset = ExtendedUser.objects.all()
    serializer_class = ExtendedUserSerializer

    def create(self, request, *args, **kwargs):
        username = request.DATA['username']
        password = request.DATA['password']

        try:
            ExtendedUser().create(username, password)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExtendedUserDetail(RetrieveUpdateDestroyAPIView):
    model = ExtendedUser
    serializer_class = ExtendedUserSerializer


class Me(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            raise Http404()

        user = request.user.extended_user

        return Response({
            'username': user.username
        })
