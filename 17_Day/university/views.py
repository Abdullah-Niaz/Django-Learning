from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include

def home(request):
    return render(request,'base.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')