from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from Schedule.models import Schedule, Entry
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def schedule(request):
	user = request.user
	try:
		schedule = get_object_or_404(Schedule, pk=user)
	except:
		schedule = []
	entries = []

	for day in range(7):
		entries.append(Entry.get_objects_by_day(day=day, schedule=schedule))

	return render_to_response('schedule/schedule.html', {'name':user.first_name, 'entries':entries})
