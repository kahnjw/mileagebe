from rest_framework.serializers import HyperlinkedModelSerializer, CharField
from django.contrib.auth.models import User

from extended_user.models import ExtendedUser


class ExtendedUserSerializer(HyperlinkedModelSerializer):
    username = CharField()
    password = CharField()

    class Meta:
        fields = ('url', 'username', 'password', 'access_token', 'user')
        model = ExtendedUser


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
