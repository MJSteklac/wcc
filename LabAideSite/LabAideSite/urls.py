from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'LabAideSite.views.home', name='home'),
    # url(r'^LabAideSite/', include('LabAideSite.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'LabAideSite.views.home'), 
    url(r'^login/$', 'LabAideSite.views.login'),
    url(r'^_login/$', 'LabAideSite.views._login'),
    url(r'^_logout/$', 'LabAideSite.views._logout'),
    url(r'^ChangePassword/$', 'LabAideSite.views.change_password'),
    url(r'^_ChangePassword/$', 'LabAideSite.views._change_password'),

    url(r'^schedule/', include('Schedule.urls')),
    url(r'^timesheet/', include('TimeSheet.urls')),
)
