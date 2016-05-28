from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
	username= ""
	password= ""
	print request.POST
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		state="Please login"
		user = authenticate(username = username, password = password )
		if user is not None:
			print user.is_active
			login(request,user)
			return HttpResponse("Succes")
		else:
			state="Username or password incorrect."
			print state
			return render(request,'auth/login.html')


	else:
		#render(request, 'auth/login.html')
		return render(request,'auth/login.html')

def registration(request):
	username=""
	password=""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = User.objects.create_user(username=username, password=password)
		return HttpResponse("Succes")
	else:
		return HttpResponse("Fail")

