from django.conf.urls import patterns, url

from strava_client.views import StravaUser, StravaActivities


urlpatterns = patterns(
    '',
    url(r'me/?$', StravaUser.as_view(), name='strava-me'),
    url(r'activities/?$', StravaActivities.as_view(), name='strava-activites')
)
