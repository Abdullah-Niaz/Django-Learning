from django import forms


class CustomerRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    age = forms.CharField()
    married = forms.CheckboxInput(attrs={'id': 'checkbox'})
    