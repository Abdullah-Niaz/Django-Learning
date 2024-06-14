from typing import Any
from django import forms
from django.core import validators

class DeleteData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(20), 
                            validators.MinLengthValidator(5)], error_messages={
                           "required": "Enter To Continue"}, max_length=20)

class ShopForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(20), 
                            validators.MinLengthValidator(5)], error_messages={
                           "required": "Enter To Continue"}, max_length=20)
    email = forms.CharField(
        error_messages={"required": "Enter To Continue"}, max_length=20)

    def clean_name(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data['name']
        if (len(valName) < 5):
            raise forms.ValidationError("Enter the Name More than 5 Charc")
        return valName

    def clean_email(self):
        val_email = self.cleaned_data.get('email')
        if val_email is None:
            raise forms.ValidationError("Email is required.")
        if len(val_email) < 12:
            raise forms.ValidationError(
                "Enter an email with more than 12 characters.")
        return val_email

    # def clean(self):
    #     cleaned_data =  super().clean()
    #     val_name = self.cleaned_data.get("name")
    #     if val_name is None:
    #         raise forms.ValidationError("Email is required Enter to Continue.")
    #     if ( len(val_name) < 5):
    #         raise forms.ValidationError("Name Must be Greater than 5 Character")
    #     val_email = self.cleaned_data.get('email')
    #     if val_email is None:
    #         raise forms.ValidationError("Email is required. Enter to Continue")
    #     if( len(val_email) < 14):
    #         raise forms.ValidationError("Email must be greater than 12 Character")

    #     return cleaned_data
