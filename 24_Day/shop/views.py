from django.shortcuts import render

from .forms import *
from .models import * 
# Create your views here.

def rdelete(request):
    if(request.method == 'POST'):
        f = DeleteData(request.POST)  
        if(f.is_valid()):
            name = f.cleaned_data['name']
            reg = ShopFormData(name=name)
            reg.delete()
    else:
        f = DeleteData()
    return render(request, "del.html",{"form":f})

def home(request):
    if(request.method == 'POST'):
        f = ShopForm(request.POST)
        if(f.is_valid()):
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            reg  = ShopFormData(name=name,email = email)
            reg.save()
        # f = ShopForm()

    else:
        f = ShopForm()
    return render(request,"homepage.html",{"form":f})