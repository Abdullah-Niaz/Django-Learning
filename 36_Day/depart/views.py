from django.shortcuts import render
from .models import StudentInfo

# Create your views here.


def home(request):
    # student_data = StudentInfo.objects.all()
    # student_data = StudentInfo.objects.filter(marks__gte = 33)
    # student_data = StudentInfo.objects.exclude(marks__gte=33)
    # student_data = StudentInfo.objects.order_by("id")
    student_data = StudentInfo.objects.order_by("id").reverse()[:5]
    quer = student_data.query
    return render(request, "home.html",{"student_data":student_data,"query":quer})