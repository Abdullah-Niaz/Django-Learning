from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.

def studentForm(request):
    if(request.method =='POST'):
        f = StudentRegistrationForm(request.POST)
        if(f.is_valid()):
            name = f.cleaned_data['stu_name']
            email = f.cleaned_data['email']
            password = f.cleaned_data['password']
            print(name)
            f.save()
        f = StudentRegistrationForm()
    else:
        f = StudentRegistrationForm()
    return render(request,'shop/studentForm.html',{"form":f})


def teacherForm(request):
    if(request.method =='POST'):
        f = TeacherRegistrationForm(request.POST)
        if(f.is_valid()):
            # f = User('teacher_name','email','password')
            f.save()
        f = TeacherRegistrationForm()
    else:
        f = TeacherRegistrationForm()
    return render(request,'shop/teacherForm.html',{"form":f})

