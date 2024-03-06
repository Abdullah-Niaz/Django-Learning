from django.shortcuts import render
from django.http import HttpResponse

def junvary(request):
    return HttpResponse("Hello This is working fine")


def weAreDone(request):
    return HttpResponse("<h1>We are done with it and working fine everything</h1> <a href='http://127.0.0.1:8000/cha_app/junvary'>Home </a>")
# Create your views here.
