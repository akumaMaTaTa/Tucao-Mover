from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
	#cookie = request.COOKIES.get('key','default')
	print request.user.is_authenticated()
	if request.user.is_authenticated():

	#if cookie!='default':
		# redirect to homepage
		user = request.user
		return HttpResponse("homepage user %s" % str(user))
	else:
		#redirect to login
		return redirect('login')
		#return HttpResponse("login")