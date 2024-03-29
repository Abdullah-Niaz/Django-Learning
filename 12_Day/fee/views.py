from django.shortcuts import render
from django.http  import HttpResponseRedirect, JsonResponse, HttpResponse

# Create your views here.

def fee(request):
    return render(request,'fee/home.html')

data = {
    '1': "<h1>Day 1</h1>"
}

def dynamic(request,route):
    if route == 1:
        return HttpResponse(data['1'])