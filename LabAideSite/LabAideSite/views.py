from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
	user = request.user
	return render_to_response('home.html', {'name':user.first_name})

def login(request):
	return render(request, 'login.html', {})

def _login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login_auth(request, user)
			return render_to_response('success.html', {'name':user.first_name})
		else:
			return render_to_response('login.html', {})

	return render_to_response('login.html', {})

def _logout(request):
	logout_auth(request)
	return render_to_response('success.html', {})
