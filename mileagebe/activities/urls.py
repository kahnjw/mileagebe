from django.conf.urls import patterns, url

from activities.views import ActivityList, ActivityDetail


urlpatterns = patterns(
    '',
    url(r'$', ActivityList.as_view(), name='activity-list'),
    url(r'(?P<pk>\d+)/?$', ActivityDetail.as_view(), name='activity-detail')
)
