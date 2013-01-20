from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'LabAideSite.views.home', name='home'),
    # url(r'^LabAideSite/', include('LabAideSite.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'LabAideSite.views.home'), 
)
