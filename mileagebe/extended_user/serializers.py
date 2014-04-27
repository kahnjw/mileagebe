from rest_framework import serializers

from extended_user.models import ExtendedUser


class ExtendedUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = ('url', 'username', 'password', 'gear', 'activities')
        write_only_fields = ('password', )
        read_only_fields = ('gear', 'activities')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
