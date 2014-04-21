from rest_framework.serializers import HyperlinkedModelSerializer

from extended_user.models import ExtendedUser


class ExtendedUserSerializer(HyperlinkedModelSerializer):

    class Meta:
        fields = ('url', 'username', 'password')
        write_only_fields = ('password', )
        model = ExtendedUser
