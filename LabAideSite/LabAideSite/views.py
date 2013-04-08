from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
	user = request.user
	return render_to_response('home.html', {'user':user})

def login(request):
	return render(request, 'login.html', {})

def _login(request):
	username = request.POST['username']
	password = request.POST['password']
	try:
		user = authenticate(username=username, password=password)
	except:
		user = None

	if user is not None:
		if user.is_active:
			login_auth(request, user)
			return home(request)
		else:
			return login(request)

	return login(request)

@login_required(login_url='/login/')
def _logout(request):
	logout_auth(request)
	return home(request)

@login_required(login_url='/login/')
def change_password(request):
	return render(request, 'change_password.html', {})

@login_required(login_url='/login/')
def _change_password(request):
	user = request.user
	user.set_password(request.POST['password'])
	user.save()
	return home(request)
