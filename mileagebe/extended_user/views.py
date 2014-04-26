from django.contrib.auth import logout
from django.http import Http404
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response

from extended_user.models import ExtendedUser
from extended_user.serializers import ExtendedUserSerializer


class ExtendedUserList(ListCreateAPIView):
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


class SessionLogout(APIView):
    def get(self, request):
        logout(request)
        return redirect('/')
