from django.shortcuts import render

# Create your views here.

def fee_home(request):
    dic = {
        'item1': 'value1',
        'item2': 'value2',
        'item3': 'value3',
    }
    return render(request,'fee/home.html',{'dic':dic})
