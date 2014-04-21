from django.conf.urls import patterns, url

from .views import Session, AuthCheck


urlpatterns = patterns(
    '',
    url(r'auth-check/?$', AuthCheck.as_view(), name='auth-check'),
    url(r'$', Session.as_view(), name='user-auth'),
)
