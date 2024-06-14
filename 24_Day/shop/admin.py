from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(ShopFormData)

class ShopFormDataAdmin(admin.ModelAdmin):
    list_display = ['name','email']