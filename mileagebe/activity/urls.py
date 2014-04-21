from django.conf.urls import patterns, url

from activity.views import SocialUserList


urlpatterns = patterns(
    '',
    url(r'$', SocialUserList.as_view(), name='extendeduser-list')
)
