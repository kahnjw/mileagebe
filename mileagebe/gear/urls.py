from django.conf.urls import patterns, url

from gear.views import GearList, GearDetail


urlpatterns = patterns(
    '',
    url(r'(?P<pk>\d+)/?$', GearDetail.as_view(), name='gear-detail'),
    url(r'$', GearList.as_view(), name='gear-list'),
)
