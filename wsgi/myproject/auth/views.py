from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 

# Create your views here.
def login_user(request):
	username= ""
	password= ""
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password )
		if user:
			login(request,user)
			return HttpResponse("Succes")
		else:
			return HttpResponse("Fail")
