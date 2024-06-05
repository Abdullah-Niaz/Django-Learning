from django.shortcuts import render

# Create your views here.

fee_urls ={
    "fee":"/fee/",
    "feestructure": "/feestructure/"
}
shop = 'shop'

def fee(request):
    return render(request, 'fee.html')

def feestructure(request):
    return render(request, 'feestructure.html')
