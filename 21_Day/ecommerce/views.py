from django.shortcuts import render



default_urls = {
    "home": "/home/",
    "about": "/about/",
    "contact": "/contact/",
    "blog": "/blog/"
}

def home(request):
    return render(request, 'home.html', {"df_urls": default_urls})

def about(request):
    return render(request, 'about.html', {"df_urls": default_urls})

def contact(request):
    return render(request, 'contact.html', {"df_urls": default_urls})

def blog(request):
    return render(request, 'blog.html', {"df_urls": default_urls})