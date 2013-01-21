from django.conf.urls import patterns, include, url

urlpatterns = patterns('Schedule.views',

    url(r'^$', 'schedule'), 
)
