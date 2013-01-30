from django.conf.urls import patterns, include, url

urlpatterns = patterns('TimeSheet.views',
	url(r'^$', 'index'), 
	url(r'^(?P<payperiod>\d+)/$', 'view'),
	url(r'^(?P<payperiod>\d+)/add_entry', 'add_entry'),
	url(r'^(?P<payperiod>\d+)/_save', '_save'),
)
