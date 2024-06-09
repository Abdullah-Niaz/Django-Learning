from django.shortcuts import render

from  .models import *
from .forms import *
# Create your views here.

fee_urls ={
    "fee":"/fee/",
    "feestructure": "/feestructure/"
}
shop = 'shop'

def showFormData(request):
    if(request.method=='POST'):
        print("Request is coming from Post Method")
        fm = FormRegistration(request.POST)
        if(fm.is_valid()):
            name = fm.cleaned_data['username']
            Email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(f"""
                    Cleaned Data 
                    Name:  {name}
                    Email: {Email}
                    Password: {password}""".format(name,Email,password))
            result = {
                        "name":name,
                        "email":Email,
                        "password":password
                    }
    else:
        fm = FormRegistration()
        print("Request is coming from Get Method")
    return render(request,'showFormData.html',{"form":fm,"result":result})

def fee(request):
    sh = EcommerceProduct.objects.all().values()
    f = FormRegistration()
    return render(request, 'fee.html',{"shop":sh,"f":f})

def feestructure(request):
    return render(request, 'feestructure.html')
