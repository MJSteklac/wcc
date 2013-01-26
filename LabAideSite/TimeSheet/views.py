from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from TimeSheet.models import PayPeriod, TimeSheet, Entry
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
	user = request.user
	periods = get_list_or_404(PayPeriod)

	return render_to_response('timesheet/index.html', {'name':user.first_name, 'periods':periods})

@login_required(login_url='/login/')
def view(request, timesheet_id):
	user = request.user

	try:
		timesheet = TimeSheet.objects.get(period=timesheet_id, user=user)
	except:
		return render_to_response('timesheet/view.html', {'name':user.first_name, 'dne':"True"})

	entries = get_list_or_404(Entry, timesheet=timesheet)
	return render_to_response('timesheet/view.html', {'name':user.first_name, 'dne':"False", 'entries':entries})

@login_required(login_url='/login/')
def add_entry(request, timesheet_id):
	user = request.user
	return render(request, 'timesheet/add_entry.html', {'name':user.first_name})

def _save(request, timesheet_id):
	user = request.user
	try:
		ts = TimeSheet.objects.get(pk=timesheet_id, user=user)
	except:
		pp = PayPeriod.objects.get(period=timesheet_id)
		ts = TimeSheet(period=pp, user=user)
		ts.save()

	entry = Entry(timesheet=ts, week=request.POST['week'], class_name=request.POST['class_name'], day=request.POST['day'], start=request.POST['start'], end=request.POST['end'], comments=request.POST['comments'])
	entry.save()
	return render_to_response('success.html', {'name':user.first_name})



