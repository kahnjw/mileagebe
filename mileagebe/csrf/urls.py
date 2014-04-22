from django.conf.urls import patterns, url

from csrf.views import Csrf


urlpatterns = patterns(
    '',
    url(r'$', Csrf.as_view(), name='csrf'),
)
