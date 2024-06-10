from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from  .models import *
from .forms import *
# Create your views here.

fee_urls ={
    "fee":"/fee/",
    "feestructure": "/feestructure/"
}
shop = 'shop'

def succesfulDataSubmission(request):
    return render(request, "success.html")


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
        
        return HttpResponseRedirect("/shop/success/")
    else:
        fm = FormRegistration()
        print("Request is coming from Get Method")
    return render(request,'showFormData.html',{"form":fm})

def fee(request):
    sh = EcommerceProduct.objects.all().values()
    f = FormRegistration()
    return render(request, 'fee.html',{"shop":sh,"f":f})

def feestructure(request):
    return render(request, 'feestructure.html')
