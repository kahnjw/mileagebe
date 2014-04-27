from django.conf.urls import patterns, url

from extended_user.views import (ExtendedUserDetail, ExtendedUserList, Me,
                                 Session)


urlpatterns = patterns(
    '',
    url(r'me/?$', Me.as_view(), name='me'),
    url(r'session/?$', Session.as_view(), name='session'),
    url(r'(?P<pk>\d+)/?$', ExtendedUserDetail.as_view(),
        name='extendeduser-detail'),
    url(r'$', ExtendedUserList.as_view(), name='extendeduser-list')
)
