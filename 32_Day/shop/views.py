from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'Rahul'
    request.session['age'] = '21'
    return render(request,"setsession.html")
def getsession(request):
    name = request.session.get("name",default="Guest")
    age = request.session.get('age',default="None")
    cl = request.session.setdefault("Phone","+96")
    items = request.session.items()
    keys = request.session.keys()
    return render(request,"getsession.html",{'name':name,'age':age,"keys":keys,"items":items,"default":cl})

def delsession(request):
    # if 'name' and 'age' in request.session:
    #     del request.session['name']
    #     del request.session['age']
    # else:
    #     f  = "No Cookies avaiable to delele"
    request.session.flush()
    return render(request,"deletesession.html")
    # return render(request, "deletesession.html")