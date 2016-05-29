from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
	username= ""
	password= ""
	print request.POST
	state="Please login"
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username = username, password = password )
		# log in succes
		if user is not None:
			login(request,user)
			return HttpResponse("Succes")
		# log in failed
		else:
			state="Username or password incorrect."
			return render(request,'auth/login.html')


	else:
		return render(request,'auth/login.html')

def registration(request):
	username=""
	password=""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		print username,password
		try:
			user = User.objects.create_user(username,email,password)
			print user
		except Exception,e:
			print e
		
		return HttpResponse("Succes")
	else:
		return render(request,'auth/registration.html')

