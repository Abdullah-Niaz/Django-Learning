from django.shortcuts import render
from shop.models import *
from shop.forms import *


default_urls = {
    "home": "/home/",
    "about": "/about/",
    "contact": "/contact/",
    "blog": "/blog/"
}

def home(request):
    sh = EcommerceProduct.objects.all().values()
    f = FormRegistration(auto_id='some_%s',label_suffix='-',field_order=['name','email',])
    print(dir(f))
    return render(request, 'home.html', {"df_urls": default_urls,"shop":sh,"f":f})

def about(request):
    return render(request, 'about.html', {"df_urls": default_urls})

def contact(request):
    return render(request, 'contact.html', {"df_urls": default_urls})

def blog(request):
    return render(request, 'blog.html', {"df_urls": default_urls})