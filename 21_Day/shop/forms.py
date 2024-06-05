from django import forms

class FormRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()