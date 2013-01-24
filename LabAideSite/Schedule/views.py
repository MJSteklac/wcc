from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from Schedule.models import Schedule, Entry
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def schedule(request):
	user = request.user
	schedule = get_object_or_404(Schedule, pk=user)
	entries = get_list_or_404(Entry, schedule=schedule)

	mon = []
	tue = []
	wed = []
	thu = []
	fri = []
	sat = []
	sun = []

	for entry in entries:
		if entry.day == 0:
			mon.append(entry)
		elif entry.day == 1:
			tue.append(entry)
		elif entry.day == 2:
                        wed.append(entry)
		elif entry.day == 3:
                        thu.append(entry)
		elif entry.day == 4:
                        fri.append(entry)
		elif entry.day == 5:
                        sat.append(entry)
		elif entry.day == 6:
                        sun.append(entry)

	return render_to_response('schedule/schedule.html', {'name':user.first_name, 'mon':mon, 'tue':tue, 'wed':wed, 'thu':thu, 'fri':fri, 'sat':sat, 'sun':sun})
