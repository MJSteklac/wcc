from django.conf.urls import patterns, include, url

urlpatterns = patterns('TimeSheet.views',
	url(r'^$', 'index'), 
	url(r'^(?P<payperiod>\d+)/$', 'view'),
	url(r'^(?P<payperiod>\d+)/add_entry', 'add_entry'),
	url(r'^(?P<payperiod>\d+)/_save', '_save'),
	url(r'^(?P<payperiod>\d+)/_delete/(?P<primary_key>\d+)', '_delete'),
	url(r'^all/$', 'index'),
	url(r'^all/(?P<payperiod>\d+)/$', 'display_users'),
	url(r'^all/(?P<payperiod>\d+)/(?P<username>.+)', 'view_for_user'),
)
