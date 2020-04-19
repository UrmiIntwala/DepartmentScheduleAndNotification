from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from myProj.models import UserDetails
from django.db import connection
from django.shortcuts import render_to_response
from TimeTable.models import TimeTable
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
	def get (self, request, **kwargs):
		return render(request, 'index.html', context=None)

def login(request):
	return render(request, 'index.html')

def validatestudent(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user1 = UserDetails.objects.filter(user=username)
	if user1 is not None:
		for u in user1:
			if u.pwd!=password:
				msg="Incorrect password"
				return render_to_response('index.html',{'message':msg})
		request.session["role"]="student"
		return render_to_response('student.html',{'studentid':username})
	else:
		return render(request,'index.html')

		
def validateUser(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user1 = UserDetails.objects.filter(user=username)
	if user1 is not None:
		for u in user1:
			if u.pwd!=password:
				msg="Incorrect password"
				return render_to_response('index.html',{'message':msg})
	
		request.session["role"]="faculty"
		request.session["username"]=username
		#added
		#role=request.session.get["role"]
		#if role=="faculty":
		facultyname=request.session["username"]
		info_1 = TimeTable.objects.filter(faculty= facultyname)
		print(info_1)
			
		#else:
		#	return render(request,'index.html')
		#added end
		subject=request.POST.get("subjectsearch")
		info2=TimeTable.objects.filter(subject=subject)
		return render_to_response('admin.html', {'infofaculty':info_1},{'infosubject':info2})
	else:
		msg="User doesnot exist"
		return render_to_response('index.html',{'message',msg})

def timetable_faculty(request):
	role=request.session["role"]
	if role=="faculty":
		facultyname=request.session["username"]
		info_1 = TimeTable.objects.filter(faculty = "CKB")
		print(info_1)
		return render_to_response('admin.html', {'infofaculty':info_1})
	else:
		return render(request,'index.html')
	
def timetable_subject(request):
	searchname = request.POST.get('subject', '')
	info_1 = TimeTable.objects.filter(subject = searchname)
	return render_to_response('admin.html', {'infosubject':info_1})

def timetable_class(request):
	searchname = request.POST.get('classname', '')
	searchname_1 = request.POST.get('facultynamename', '')
	username=request.session.get["username"]
	role=request.session.get["role"]
	info_1 = TimeTable.objects.filter(faculty_name = searchname, class_name = searchname_1)
	return render_to_response('admin.html', {'info':info_1})

def insert_timetable(request):
	branch=request.POST.get('branch', '')
	year=request.POST.get('year', '')
	division=request.POST.get('division', '')
	day=request.POST.get('day', '')
	subject=request.POST.get('subject', '')
	time=(request.POST.get('time', ''))
	classroom=request.POST.get('classroom', '')
	faculty=request.POST.get('faculty', '')
	timetable = TimeTable(branch=branch, year=year, division=division, day=day, subject=subject, time=time, classroom=classroom, faculty=faculty)
	timetable.save()
	return render(request, 'admin.html')
