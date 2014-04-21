from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/v1/users/', include('extended_user.urls')),
    url(r'^api/v1/csrf/?$', include('csrf_resource.urls')),
    url(r'^api/v1/auth/', include('auth.urls')),
    url(r'^api/v1/social-auth/',
        include('social.apps.django_app.urls', namespace='social'))
    # Examples:
    # url(r'^$', 'stompnet.views.home', name='home'),
    # url(r'^stompnet/', include('stompnet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
