from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from myProj.models import UserDetails

# Create your views here.
class HomePageView(TemplateView):
	def get(self,request,**kwargs):
		return render(request,'index.html',context=None)

def login(request):
	return render(request,'login.html')

def validateUser(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user = authenticate(username=username, password=password)
	request.session["username"] = username
	if user is not None:
		request.session["role"]=user.role
	else:
		return render(request,'Login.html')
