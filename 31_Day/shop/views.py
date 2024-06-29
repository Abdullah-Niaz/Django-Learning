from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def setcookies(request):
    response = render(request, "setcookies.html")
    response.set_cookie("name", "abdullah")
    return response


def getcookies(request):
    # response = request.COOKIES['name']
    response = request.COOKIES.get('ame','Guest')
    response = request.COOKIES.get('name','Guest')
    return render(request, "getcookies.html", {"response": response})


def delcookies(request):
    response =render(request,"deletecookies.html")
    x = response.delete_cookie("name")
    return render(request,"deletecookies.html",{"response":x})
