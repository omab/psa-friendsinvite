from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('friendsinvite.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
)
