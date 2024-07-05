from django.shortcuts import render
from django.core.cache import cache

def home(request):
    mv = cache.get_or_set("fee","paid",10)
    return render(request, "home.html",{"mv":mv})