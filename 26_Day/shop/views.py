from django.shortcuts import render

# Create your views here


def ghar(request):
    return render(request,"ghar.html")

def home(request,route):
    if route == "home":
        route = "This is the Home Page of shop App"
    if route == "about":
        route = "This is the about Page of shop App"
    if route == "contact":
        route = "This is the contact Page of shop App"
    if route == "blog":
        route = "This is the blog Page of shop App"
    return render(request,"home.html",{"r":route})