from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns(
    '',
    url(r'^api/v1/users/', include('extended_user.urls')),
    url(r'^api/v1/csrf/?$', include('csrf.urls')),
    url(r'^api/v1/social-auth/',
        include('social.apps.django_app.urls', namespace='social')),
    url(r'^api/v1/', include('strava_client.urls')),
    url(r'^api/v1/gear/', include('gear.urls')),
    url(r'^api/v1/activities/', include('activities.urls'))
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
