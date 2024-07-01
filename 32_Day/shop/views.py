from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session['name'] = 'Rahul'
    request.session['age'] = '21'
    return render(request,"setsession.html")
def getsession(request):
    # name = request.session['name']
    # age = request.session['age']
    name = request.session.get("nam",default="Guest")
    age = request.session.get('ag',default="None")
    return render(request,"getsession.html",{'name':name,'age':age})

def delsession(request):
    if 'name' and 'age' in request.session:
        del request.session['name']
        del request.session['age']
    else:
        f  = "No Cookies avaiable to delele"
    
    return render(request,"deletesession.html", {"f":f})
    # return render(request, "deletesession.html")