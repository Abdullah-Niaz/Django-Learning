from django.shortcuts import render

# Create your views here.

def departhome(request):
    return render(request,'depart/home.html')
