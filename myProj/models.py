from djongo import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
	user = models.CharField(primary_key=True,max_length=10)
	pwd = models.CharField(max_length=10)
	role=models.CharField(max_length=50)

class Student(models.Model):
	student_id=models.CharField(primary_key=True , max_length=10,default="")
	student_name = models.CharField(max_length=100,default="")
	student_dob = models.DateTimeField
	student_emailid=models.EmailField
	student_phonenumber=models.IntegerField
	student_year=models.IntegerField
	student_branch=models.CharField(max_length=2,default="")
	student_div=models.CharField(max_length=1,default="")

class Faculty(models.Model):
	faculty_name=models.CharField(max_length=25,default="")
	faculty_init=models.CharField(max_length=4,default="")
	faculty_email=models.EmailField
	faculty_phonenumber=models.IntegerField
	faculty_branch=models.CharField(max_length=2,default="")


#time table - class year div faculty sub time roomno 
