from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include

def default_home(request):
    return HttpResponse("Hey! You're on a home page of the Django Server Go to the Shop Page<br> <button><a href='http://127.0.0.1:8000/shop/home/'>Shop Page</a></button>")