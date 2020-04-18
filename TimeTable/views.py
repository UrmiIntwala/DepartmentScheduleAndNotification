from django.shortcuts import render_to_response
from django.shortcuts import render
from TimeTable.models import TimeTable
# Create your views here.
from django.http import HttpResponse
def timetable_faculty(request):
	searchname = request.POST.get('facultyname', '')
	info_1 = TimeTable.objects.filter(faculty_name = searchname)
	return render_to_response('displaystudent.html', {'info':info_1})
	
def timetable_class(request):
	searchname = request.POST.get('classname', '')
	info_1 = TimeTable.objects.filter(faculty_name = searchname)
	return render_to_response('displaystudent.html', {'info':info_1})

def timetable_faculty_class(request):
	searchname = request.POST.get('classname', '')
	searchname_1 = request.POST.get('facultynamename', '')
	info_1 = TimeTable.objects.filter(faculty_name = searchname,class_name=searchname_1)
	return render_to_response('displaystudent.html', {'info':info_1})