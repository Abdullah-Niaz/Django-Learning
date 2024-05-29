from django.shortcuts import render

# Create your views here.

def fee_home(request):
    dic = {
        'item1': 'value1',
        'item2': 'value2',
        'item3': 'value3',
    }
    return render(request,'fee/home.html',{'dic':dic})


def feestructure(request):
    return render(request,'fee/feestructure.html',{"feestr":"/fee/feestructure"})
def feeplans(request):
    return render(request,'fee/feeplans.html')
def relaxation(request):
    return render(request,'fee/relaxation.html')
