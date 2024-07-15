from django.db import models

# Create your models here.
 
class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True,null=False)
    email = models.EmailField(max_length=100)
    marks = models.IntegerField()
    pass_date = models.DateField()
    