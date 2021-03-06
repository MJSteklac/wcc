# Awesome, assorted shortcuts
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404

# Import models
from TimeSheet.models import PayPeriod, TimeSheet, Entry, Category
from django.contrib.auth.models import User

# Import decorators
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required(login_url='/login/')
def index(request):
	user = request.user
	try:
		periods = get_list_or_404(PayPeriod)
	except:
		periods = []

	return render_to_response('timesheet/index.html', {'user':user, 'periods':periods})

@login_required(login_url='/login/')
def view(request, payperiod):
	user = request.user
	try:
		categories = get_list_or_404(Category)
	except:
		categories = None

	try:
		timesheet = TimeSheet.objects.get(period=payperiod, user=user)
		entries = get_list_or_404(Entry, timesheet=timesheet)
	except:
		entries = None

	return render(request, 'timesheet/view.html', {'user':user, 'entries':entries, 'categories':categories})

@login_required(login_url='/login/')
def add_entry(request, payperiod):
	user = request.user
	return render(request, 'timesheet/add_entry.html', {'user':user})

def _save(request, payperiod):
	user = request.user
	period = PayPeriod.objects.get(period=payperiod)
	category = Category.objects.get(name=request.POST['category'])
	ts, created = TimeSheet.objects.get_or_create(period=period, user=user)
	if created:
		ts.save()

	entry = Entry(timesheet=ts, category=category, start=request.POST['start'], end=request.POST['end'], comments=request.POST['comments'], date=request.POST['date'])
	entry.save()
	return view(request, payperiod)

def _delete(request, primary_key, payperiod):
	entry = get_object_or_404(Entry, pk=primary_key)
	entry.delete()
	return view(request, payperiod)

@staff_member_required
def display_users(request, payperiod): 
	user = request.user
	users = User.objects.all()
	return render_to_response('timesheet/admin/users.html', {'user':user, 'users':users})

@staff_member_required
def view_for_user(request, payperiod, username):
	user = request.user
	user_to_load = User.objects.get(username=username)
	try:
		timesheet = TimeSheet.objects.get(user=user_to_load, period=payperiod)
	except:
		timesheet = None
	try:
		entries = get_list_or_404(Entry, timesheet=timesheet)
	except:
		entries = []

	return render_to_response('timesheet/view.html', {'user':user, 'entries':entries})
