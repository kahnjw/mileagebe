from django.conf.urls import patterns, url

from strava_client.views import StravaUser, StravaActivities, StravaGear


urlpatterns = patterns(
    '',
    url(r'me/?$', StravaUser.as_view(), name='strava-me'),
    url(r'activities/?$', StravaActivities.as_view(), name='strava-activites')
    # url(r'gear/(?P<gear_id>\w+)/?$', StravaGear.as_view(), name='strava-gear')
)
