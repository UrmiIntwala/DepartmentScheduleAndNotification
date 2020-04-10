from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from myProj.models import UserDetails
from django.db import connection

# Create your views here.
class HomePageView(TemplateView):
	def get (self, request, **kwargs):
		return render(request, 'index.html', context=None)

def login(request):
	return render(request, 'index.html')

def validateUser(request):
	username = request.POST.get('username', '')
	print(username)
	password = request.POST.get('password', '')
	print(password)
	user1 = UserDetails.objects.filter(user=username, pwd=password)
	for i in user1:
		print(i)
	request.session["username"] = username
	if user1 is not None:
		#request.session["role"]=user1.role
		return render(request, 'admin.html')
	else:
		return render(request, 'index.html')
