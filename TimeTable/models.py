from django.db import models
from djongo import models

# Create your models here.
class TimeTable(models.Model):
    branch=models.CharField(max_length=2)
    year=models.IntegerField(default=0)
    division=models.CharField(max_length=1)
    day=models.CharField(max_length=3,default="")
    subject=models.CharField(max_length=20)
    time=models.CharField(max_length=5,default="00:00")
    classroom=models.CharField(max_length=2,default="")
    faculty=models.CharField(max_length=4)
    class Meta:
        unique_together = (('branch', 'division','day','time','year'),)