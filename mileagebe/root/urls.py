from django.conf.urls import patterns, url

from root.views import Root


urlpatterns = patterns(
    '',
    url(r'$', Root.as_view(), name='api-root')
)
