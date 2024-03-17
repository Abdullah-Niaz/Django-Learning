from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

shopname = {"name":"Ecommerce Shop for Everyone"}

def home(request):
    return render(request,"shop/basic_nav.html",context=shopname)
