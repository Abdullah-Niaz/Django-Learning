from django.shortcuts import render
from django.http  import HttpResponseRedirect, JsonResponse, HttpResponse

def myhome(request):
    return HttpResponse("Hello World")