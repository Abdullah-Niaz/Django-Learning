from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def departments(request):
    return HttpResponse("Department app")
