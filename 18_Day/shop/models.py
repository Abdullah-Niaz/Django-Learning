from django.db import models

# Create your models here.

class student(models.Model):
    stuid = models.IntegerField()
    stuName =  models.CharField(max_length=70)
    stuAddress = models.CharField(max_length=70)
    stuMessage = models.CharField( max_length=50,default="NAN")

    # def __str__(self) -> str:
    #     return student.objects.all().values()
    # def __str__(self) -> str:
    #     return self.stuid