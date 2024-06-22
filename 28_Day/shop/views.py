from django.shortcuts import render
from django.contrib import messages
from .forms import *
# Create your views here.


def registration(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if(fm.is_valid()):
            fm.save()
            messages.add_message(request,messages.SUCCESS,'Ho Gea Bahi Submit')
    else:
        fm = Registration()
    return render(request, "shop/regestration.html",{'form':fm})