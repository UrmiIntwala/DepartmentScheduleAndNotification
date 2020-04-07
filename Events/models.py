from djongo import models
from django import forms
from myProj.models import Student

# Create your models here.
class Events(models.Model):
    event_name=models.CharField(max_length=20)
    event_descr=models.CharField
    event_venue=models.CharField
    event_date=models.DateField
    event_organizer=models.CharField
    participants_list=models.ArrayModelField(
        model_container=Student
    )
    