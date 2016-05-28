from django.conf.urls import include, url

from . import views
urlpatterns = [
	url(r'^login/', views.login_user, name='login'),
	url(r'^signup/',views.registration, name='signup')
]