from django.shortcuts import render
from .forms import *
# Create your views here.


def home(request):
    if (request.method == 'POST'):
        p = ShopForm.objects.get(pk=1)
        f = ShopFormData(request.POST,instance=p)
        if (f.is_valid()):
            f.save()
            # name = f.cleaned_data['name']
            # email = f.cleaned_data['email']
            # password = f.cleaned_data['password']

            # print(f""""Name:  {name}
            #            Email: {email}
            #     """.format(name, email))
            # reg = ShopForm(name=name,email = email,password=password)
            # reg.save()
        # f = ShopFormData()

    else:
        f = ShopFormData()
    fdata = ShopForm.objects.all().values()
    return render(request, "home.html", {"form": f, "Data": fdata})
