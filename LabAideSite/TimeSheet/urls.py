from django.conf.urls import patterns, include, url

urlpatterns = patterns('TimeSheet.views',
	url(r'^$', 'index'), 
	url(r'^(?P<timesheet_id>\d+)/$', 'view'),
	url(r'^(?P<timesheet_id>\d+)/add_entry', 'add_entry'),
	url(r'^(?P<timesheet_id>\d+)/_save', '_save'),
)
