from django import forms


class ShopRegistrationFrom(forms.Form):
    name = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=30)
    img = forms.ImageField()