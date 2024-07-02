from django.shortcuts import render

# Create your views here.

def setsession(request):
    request.session.set_expiry(0)
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    request.session['name'] = 'Rahul'
    request.session['age'] = '21'
    return render(request,"setsession.html")
def getsession(request):
    age = request.session.get_expiry_age()
    print(age/12)
    print(request.session.get_expiry_date())
    print(request.session.get_session_cookie_age())
    print(request.session.get_expire_at_browser_close())

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