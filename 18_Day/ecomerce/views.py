from django.urls import path
from django.shortcuts import render

# importing models 
from shop.models import *


def defaulthome(request):
    stu = student.objects.all().values()
    return render(request,'core.html',{'stu':stu})
    return render