from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    link = "www.google.com"
    html = f'<button><a href="">Heading</a></button>'
    return HttpResponse(html)

def service(request):
    return HttpResponse("services")


def blog(request):
    return HttpResponse("Blog")

def contact(request):
    return HttpResponse("Contact")

