from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'friendsinvite.views.home', name='home'),
    url(r'^done/$', 'friendsinvite.views.done', name='done'),
    url(r'^logout/$', 'friendsinvite.views.logout', name='logout')
)
