from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.

def sign(request):
    if(request.method == "POST"):
        fm = Usercreation(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = Usercreation()
    return render(request, "sign.html",{"form":fm})

def userlogin(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in successfully!")
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.error(request, "Invalid username or password.")
        else:
            fm = AuthenticationForm()
        return render(request, "login.html", {"form": fm})
    else:
        return HttpResponseRedirect("/profile/")

def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html",{"name":request.user})
    else:
        return HttpResponseRedirect("/userlogin/")
def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/userlogin/")