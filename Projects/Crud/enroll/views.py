from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404
from django.db import connection

from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def add_show(request):
    if(request.method=='POST'):
        f = StudentRegistration(request.POST)
        if(f.is_valid()):
            f.save()
            # or you can use 
            # name = f.cleaned_data['name']
            # email = f.cleaned_data['email']
            # password = f.cleaned_data['password']
            # r = User(name=name,email=email,password=password)
            # r.save()
        f = StudentRegistration()
    else:
        f = StudentRegistration()
    stData = User.objects.all().values()
    return render(request,"enroll/addandshow.html",{"form":f,"stData":stData})


def UpdateData(request,id):
    if (request.method=="POST"):
        pi = User.objects.get(pk=id)
        f = StudentRegistration(request.POST,instance=pi)
        if(f.is_valid()):
            f.save()
    else:
        pi = User.objects.get(pk=id)
        f = StudentRegistration(instance=pi)
    return render(request, "enroll/updatestudent.html" ,{'form':f})
def DeleteData(request,id):
    if(request.method =="POST"):
        p = User.objects.get(pk=id)
        p.delete()
        return HttpResponseRedirect("/")
