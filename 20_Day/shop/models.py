from django.db import models

# Create your models here.



class StudentData(models.Model):
    name = models.CharField(max_length=50)
    stuid = models.IntegerField()
    roll_no = models.CharField(max_length=50)
