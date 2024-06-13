from typing import Any
from django import forms
from django.core import validators

class ShopForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput())

    # check = forms.BooleanField(required=True)
    # file = forms.FileField()
    def clean(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data['name']
        if (len(valName) < 5):
            raise forms.ValidationError("Enter the Name More than 5 Charc")
        val_email = self.cleaned_data.get('email')
        if val_email is None:
            raise forms.ValidationError("Email is required.")
        if len(val_email) < 12:
            raise forms.ValidationError("Enter an email with more than 12 characters.")   


        val_pass = self.cleaned_data['password']
        rval_pass = self.cleaned_data['rpassword']
        if(val_pass != rval_pass):
            raise forms.ValidationError("Password Does not Match")
        

    # def clean_name(self):
    #     cleaned_data = super().clean()
    #     valName = self.cleaned_data['name']
    #     if (len(valName) < 5):
    #         raise forms.ValidationError("Enter the Name More than 5 Charc")
    #     return valName
    # def clean_email(self):
    #     val_email = self.cleaned_data.get('email')
    #     if val_email is None:
    #         raise forms.ValidationError("Email is required.")
    #     if len(val_email) < 12:
    #         raise forms.ValidationError("Enter an email with more than 12 characters.")
    #     return val_email
    



    # def clean_name(self):
    #     val_name= self.cleaned_data["name"]
    #     if(len(val_name)<5):
    #         raise forms.ValidationError("Enter the More than Length of 5")
    #     return val_name

    # def clean_check(self):
    #     val_check = self.cleaned_data.get('check')
    #     if not val_check:
    #         raise forms.ValidationError("Kindly Check the Form")
    #     return val_check    
