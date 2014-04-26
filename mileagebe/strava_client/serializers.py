from rest_framework.serializers import HyperlinkedModelSerializer
from social.apps.django_app.default.models import UserSocialAuth


class SocialUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserSocialAuth
