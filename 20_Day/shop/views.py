from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.



def home(request):
    m = StudentData.objects.all().values()
    f = CustomerRegistration(auto_id='shop_%s',label_suffix='')
    f.order_fields(field_order=['name','age','email','married'])
    return render(request,"core.html",{'form':f,"db":m})