from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.
dynamic_dict = {
    "home":"<h1>this is the home page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    
    "about":"<h1>this is the about page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    
    "contact":"<h1>this is the contact page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    
    "blog":"<h1>this is a blog page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>"
}  


def dynamic_str(request, route):
    try:
        reponse = dynamic_dict[route]
        return HttpResponse(reponse)
    except:
        return HttpResponseNotFound("Not Found 😢")

def dynamic_int(request,route):
    try:
        response = list(dynamic_dict.keys())
        if route > len(response):
            return HttpResponseNotFound("not Found 🤦‍♂️")
        else:
            return_response = response[route-1]
            return HttpResponseRedirect("/shop/" + return_response)
    except:
        return HttpResponseNotFound("not found in integer list")

