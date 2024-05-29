from django.urls import path
from django.shortcuts import render

def defaulthome(request):
    return render(request,'core.html')