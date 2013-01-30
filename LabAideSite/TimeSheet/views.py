from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from TimeSheet.models import PayPeriod, TimeSheet, Entry
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login/')
def index(request):
	user = request.user
	periods = get_list_or_404(PayPeriod)

	return render_to_response('timesheet/index.html', {'name':user.first_name, 'periods':periods})

@login_required(login_url='/login/')
def view(request, payperiod):
	user = request.user

	try:
		timesheet = TimeSheet.objects.get(period=payperiod, user=user)
	except:
		return render_to_response('timesheet/view.html', {'name':user.first_name, 'dne':"True"})

	entries = get_list_or_404(Entry, timesheet=timesheet)
	return render_to_response('timesheet/view.html', {'name':user.first_name, 'dne':"False", 'entries':entries})

@login_required(login_url='/login/')
def add_entry(request, payperiod):
	user = request.user
	return render(request, 'timesheet/add_entry.html', {'name':user.first_name})

@csrf_exempt
def _save(request, payperiod):
	user = request.user
	period = PayPeriod.objects.get(period=payperiod)
	ts, created = TimeSheet.objects.get_or_create(period=period, user=user)
	if created:
		ts.save()

	entry = Entry(timesheet=ts, week=request.POST['week'], class_name=request.POST['class_name'], day=request.POST['day'], start=request.POST['start'], end=request.POST['end'], comments=request.POST['comments'])
	entry.save()
	return render_to_response('success.html', {'name':user.first_name})



