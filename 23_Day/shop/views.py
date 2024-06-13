from django.shortcuts import render
from .models import *
from .forms import * 
# Create your views here.
def home(request):
    if(request.method == 'POST'):
        f = ShopRegistrationFrom(request.POST)
        if(f.is_valid()):
            name = f.cleaned_data['name']
            email = f.cleaned_data['email']
            img = f.cleaned_data['img']
            reg = ShopForm(id = 1, name=name,email=email,img=img)
            
            reg.save()
        f = ShopRegistrationFrom()
    else:
        f = ShopRegistrationFrom()
    data = ShopForm.objects.all().values()
    return render(request,'shop/home.html',{"data":data,"form":f})