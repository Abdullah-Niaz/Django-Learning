from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fee(request):
    return render(request,'fee/home.html')