from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

# Create your views here.
  
dynamic_dict = {
    "home":"<h1>this is the home page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    "about":"<h1>this is the about page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    "contact":"<h1>this is the contact page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>",
    "blog":"<h1>this is a blog page</h1><button><a href='http://127.0.0.1:8000/shop/'>Shop Home</a></button>"
}  

def dynamic_int(reuqest,route):
    try:
        response = list(dynamic_dict.keys())
        if route > len(response):
            return HttpResponseNotFound("Not found which you want ")
        return_response = response[route - 1]
        return HttpResponseRedirect("/shop/" + return_response)
    except:
        return HttpResponseNotFound("not found in integer list")


def dynamic(request , route):
    try:
        response = dynamic_dict[route]
        return HttpResponse(response)
    except:
        return HttpResponseNotFound("not found in string list")
    
    
    
    
    
    
    # response = None  
    # if(route == "home"):
    #     repsonse = ("this is home page")
    # elif(route == "about"):
    #     response = ("this is about page")
    # elif(route == "contact"):
    #     response = ("this is contact page")
    # elif(route == "blog"):
    #     response = ("this is blog page")
    # else:
    #     return HttpResponseNotFound("nothing found 404")
    # return HttpResponse(response)