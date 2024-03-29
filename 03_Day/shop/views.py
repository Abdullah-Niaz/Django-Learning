from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


# Create your views here.
def contact(request):
    return HttpResponse("This is the contact page of our site")

def dynamic_function(request,route):
    response = None
    if route == 'home':
        response = "This is my Home Paage"
    elif route== "about":
        response = "This is my about Paage"
    elif route  == "contact":
        response = "This is my contact Paage"
    elif route  == "blog":
        response = "This is my blog Paage"
    else:
        return HttpResponseNotFound("<h1 style='font-size:300px;color:blue;'>this not found</h1>")
    return HttpResponse(response)

def contactinside(request, employee_id) :
    return HttpResponse(f"<h1>{employee_id} hello, welcome to our contact page let me know how can I hlep you <br> for direct contact reach us on <a href='mailto:abdullahniaz423@gmail'>Offical Mail Center</a></h1>")