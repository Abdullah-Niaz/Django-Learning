from django.contrib import admin
from .models import *
# Register your models here.


class Registration(admin.ModelAdmin):
    list_display = ('id', 'stu_name','teacher_name', 'email', 'password')

admin.site.register(User,Registration)