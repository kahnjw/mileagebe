from django.conf.urls import patterns, url

from extended_user.views import (
    ExtendedUserDetail, ExtendedUserList, UserDetail, UserList, Me)


urlpatterns = patterns(
    '',
    url(r'me/?$', Me.as_view(), name='me'),
    url(r'system-users/?$', UserList.as_view(), name='user-list'),
    url(r'system-users/(?P<pk>\d+)/?$',
        UserDetail.as_view(), name='user-detail'),
    url(r'(?P<pk>\d+)/?$', ExtendedUserDetail.as_view(),
        name='extendeduser-detail'),
    url(r'$', ExtendedUserList.as_view(), name='extendeduser-list')
)
