from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	cookie = request.COOKIES.get('key','default')

	if not cookie == 'default':
		# redirect to homepage
		return HttpResponse("homepage cookie %s" % cookie)
	else:
		#redirect to login
		return render(request, 'auth/login.html')
		#return HttpResponse("login")