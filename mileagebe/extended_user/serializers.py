from rest_framework.serializers import HyperlinkedModelSerializer

from extended_user.models import ExtendedUser


class ExtendedUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ExtendedUser
        fields = ('url', 'username', 'password', 'gear', 'activities')
        write_only_fields = ('password', )
        read_only_fields = ('gear', 'activities')
