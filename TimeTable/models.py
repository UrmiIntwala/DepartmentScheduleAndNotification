from django.db import models
from djongo import models

# Create your models here.
class TimeTable(models.Model):
    branch=models.CharField(max_length=2)
    year=models.IntegerField
    division=models.CharField(max_length=1)
    day=models.CharField(max_length=3,default="")
    subject=models.CharField(max_length=20)
    time=models.TimeField
    classroom=models.CharField
    faculty=models.CharField(max_length=4)
    