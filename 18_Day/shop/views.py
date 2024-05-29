from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core.html')

def shop(request):
    return render(request,'shop/shop.html',{"shop":"/shop/shopdashboard"})


def shopdashboard(request):
    return render(request,'shop/shopdashboard.html')
