from django.shortcuts import render
from django.http import HttpResponse

def shop(request):
    return HttpResponse("Home Page <button><a href='http://127.0.0.1:8000/shop/about/'>About</a></button><button><a href='http://127.0.0.1:8000/shop/contact/'>Contact</a></button><button><a href='http://127.0.0.1:8000/shop/blog/'>blog</a></button> <button><a href='http://127.0.0.1:8000/'>Default Home</a></button>")
def home(request):
    return HttpResponse("Home Page <button><a href='http://127.0.0.1:8000/shop/about/'>About</a></button><button><a href='http://127.0.0.1:8000/shop/contact/'>Contact</a></button><button><a href='http://127.0.0.1:8000/shop/blog/'>blog</a></button> <button><a href='http://127.0.0.1:8000/'>Default Home</a></button>")

def about(request):
    return HttpResponse("about Page <button><a href='http://127.0.0.1:8000/shop/home/'>Home</a></button><button><a href='http://127.0.0.1:8000/shop/contact/'>Contact</a></button><button><a href='http://127.0.0.1:8000/shop/blog/'>blog</a></button> <button><a href='http://127.0.0.1:8000/'>Default Home</a></button>")

def contact(request):
    return HttpResponse("contact Page <button><a href='http://127.0.0.1:8000/shop/home/'>Home</a></button><button><a href='http://127.0.0.1:8000/shop/about/'>About</a></button><button><a href='http://127.0.0.1:8000/shop/blog/'>blog</a></button> <button><a href='http://127.0.0.1:8000/'>Default Home</a></button>")

def blog(request):
    return HttpResponse("blog Page <button><a href='http://127.0.0.1:8000/shop/home/'>Home</a></button><button><a href='http://127.0.0.1:8000/shop/about/'>About</a></button><button><a href='http://127.0.0.1:8000/shop/Contact/'>Contact</a></button> <button><a href='http://127.0.0.1:8000/'>Default Home</a></button>")


# Create your views here.
