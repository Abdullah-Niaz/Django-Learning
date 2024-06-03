from django.shortcuts import render
from django.http import HttpResponse
from  enroll.models import *

# Create your views here.
def enrolHome(request):
    stu = student.objects.all().values()
    return render(request,"enroll/enrolltemp.html",{"stu":stu})