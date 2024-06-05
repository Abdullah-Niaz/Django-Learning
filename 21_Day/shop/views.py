from django.shortcuts import render

from  .models import *
from .forms import *
# Create your views here.

fee_urls ={
    "fee":"/fee/",
    "feestructure": "/feestructure/"
}
shop = 'shop'

def fee(request):
    sh = EcommerceProduct.objects.all().values()
    f = FormRegistration()
    return render(request, 'fee.html',{"shop":sh,"f":f})

def feestructure(request):
    return render(request, 'feestructure.html')
