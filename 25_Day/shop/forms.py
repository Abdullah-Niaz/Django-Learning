from django import forms
from .models import *

class ShopFormData(forms.ModelForm):

    class Meta:
        model = ShopForm
        fields = ("name","email","password")
        labels = {"name":"Enter Name: ","email":"Enter Email: ","password":"Enter Password: "}
        error_messages = {
            "name": {"required": "Please enter your name"},
            "email": {"required": "Please enter your email"},
            "password": {"required": "Please enter your password"},
        }

        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Write your Name"}),
            "email": forms.TextInput(attrs = {"placeholder":"Write your Email"}),
            "password": forms.PasswordInput(attrs = {"placeholder":"Write your Password"}),
        }