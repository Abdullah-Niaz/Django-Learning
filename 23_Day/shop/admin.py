from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ShopForm)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','img']

# admin.site.register(ShopForm,ProductAdmin)