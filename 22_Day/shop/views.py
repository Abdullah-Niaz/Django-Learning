from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import *



# Create your views here.
def showFormSubmission(request):
    re_back = "/shop/"
    return render(request, "success.html", {"back": re_back})

def handle_uploaded_file(f):  
    with open('shop/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

def formFunc(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # file = form.cleaned_data['file']
            # handle_uploaded_file(request.FILES['file'])  
            # return HttpResponse("File uploaded successfuly")  

            # Printing the cleaned data to console
            print(name)
            print(email)
            # print(file)
            return HttpResponseRedirect('/shop/success')
    else:
        form = ShopForm()
    return render(request, "form.html", {"form": form})