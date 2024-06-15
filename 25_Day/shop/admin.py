from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ShopForm)

class ShopRegistrationForm(admin.ModelAdmin):
    list_display = ['name','email','password']